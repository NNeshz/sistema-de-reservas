from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework import status

from drf_spectacular.utils import extend_schema

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

from restaurant.models import Carrito

from .serializers import UserSerializer, UserUpdateSerializer
from .models import InviteToken 

#Checar si es necesario. (Aún no está implementado)
class UsersViewSet(ModelViewSet): #Get y Post implemented
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = UserSerializer
    update_serializer_class = UserUpdateSerializer

#CRUD user + Login + Logout + Staff Invitation

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def send_staff_invitation(request): #El token está vinculado por lo que solo funcionará cuando el usuario deseado lo active

    username = request.data.get('username', None)

    user = get_object_or_404(User, username=username) 
    
    invite_token, created = InviteToken.objects.get_or_create(user=user)
        
    invite_url = f'{request.build_absolute_uri("/invite/")}?token={invite_token.token}'
        
    print(invite_url)
    # send_mail(
    #     'Staff Invitation',
    #     f'Click the link to become a staff member: {invite_url}',
    #     settings.DEFAULT_FROM_EMAIL,
    #     [user.email],
    #     fail_silently=False,
    # )
    return Response({"message": "Invitation sent."})

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def process_staff_invitation(request):
    token = request.query_params.get('token', None)
    
    if not token:
        return Response({"error": "No token provided."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        invite_token = InviteToken.objects.get(token=token)
    except InviteToken.DoesNotExist:
        return Response({"error": "Invalid Invitation."}, status=status.HTTP_400_BAD_REQUEST)
    
    if not request.user == invite_token.user:
        return Response({"detail": "User not invited."}, status=status.HTTP_400_BAD_REQUEST)
    
    user = invite_token.user
    user.is_staff = True
    user.save()
    
    invite_token.delete()  # Invalida el token eliminándolo

    return Response({"message": "User is now a staff member."}, status=status.HTTP_200_OK)

@api_view(['POST'])
@extend_schema(
    request=UserSerializer,
    description="Create a new user and return an authentication token.",
    summary="Create User"
)
def create_user(request): 
    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid(): #Si la información recibida es válida (Contiene todos los campos requeridos, etc)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    serializer.save()

    user = User.objects.get(username=serializer.data['username']) #Obtengo el usuario comparando nombre de usuario

    token = Token.objects.create(user=user) #Genero el token
    
    # return Response({'token': token.key, 'user': serializer.data}, status.HTTP_201_CREATED)
    response = Response(status.HTTP_201_CREATED)
    response.set_cookie('token', token.key)
    response.data = {'user': serializer.data}
    
    Carrito.objects.create(user = user)
    
    return response
    
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data.get('username'))

    if not user.check_password(request.data['password']): #Sirve para comparar un string con un string ya encriptado
        return Response({'errors':'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)

    serializer = UserSerializer(instance=user)

    # return Response({'token':token.key, 'user':serializer.data}, status=status.HTTP_200_OK)
    response = Response(status.HTTP_201_CREATED)
    response.set_cookie('token', token.key)
    response.data = {'user': serializer.data}
    
    return response

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout (request):
    request.user.auth_token.delete() 
    return Response({'detail':'logout'}, status=status.HTTP_200_OK)

class UserProfileView(GenericViewSet): #Visualiza sus datos y Puede modificarlos.
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserUpdateSerializer
    def get(self, request):        
        print(f'{request.headers['Cookie'] = }')
        u = request.user
        return Response({'user': (u.username, u.email, u.is_staff)}, status.HTTP_200_OK)
    
    def put(self, request):    
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        user = request.user
        user.delete()
        return Response({'detail': 'User deleted'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def staff(request):
    users = []
    for user in User.objects.all():
        users.append(UserSerializer(instance = user).data)

    return Response ({'users':users},status=status.HTTP_200_OK)


# def get(self, request):
#     for e in (request.auth,
#         request.user,
#         request.session,
#         request.headers['Cookie'],
#         request.headers.get('Authorization', 'No authorization')):
#             print (f'{e = }')
#     print(f'{request.user.is_staff = }')
    
#     print(request.headers['Cookie'].split('; '))
    
#     return Response({'user': request.user.username}, status.HTTP_200_OK)
