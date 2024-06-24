from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import generics, ModelViewSet
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, UserUpdateSerializer
import datetime
from jose import jwt
from rest_framework.decorators import api_view
from .admin import SECRET_TOKEN_KEY  


#CRUD user + Login + Logout

def get_user_from_token(request):
    #'Authorization':'Bearer jr23oifjn3pinv4938fuoeifj'
    auth_header = request.headers.get('Authorization', None)
    if auth_header is None:
        raise AuthenticationFailed('Authorization header missing')
    
    token = auth_header.split(' ')[1]
    if not token:
        raise AuthenticationFailed('Token missing')
        
    try:
        payload = jwt.decode(token, SECRET_TOKEN_KEY, algorithms=['HS256'])
        print('Decoded payload:', payload)
        return payload
    except jwt.ExpiredSignatureError:
        print('Token has expired')
        raise AuthenticationFailed('Token has expired')
    except jwt.JWTError as e:
        print('Invalid token error:', str(e))
        raise AuthenticationFailed('Invalid token')

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'detail':'Data not valid'},status=status.HTTP_400_BAD_REQUEST)
        serializer.save()

        payload = {
            'id' : serializer.data['id'],
            'username': serializer.data['username'],
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.now()
        }

        token = jwt.encode(payload, SECRET_TOKEN_KEY, algorithm='HS256').encode('utf-8')
        
        response = Response(status=status.HTTP_201_CREATED) 
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {'token':'Is in cookies', 'user':serializer.data}

        return response

class LoginView(APIView):
    def post(self, request):
        user = get_object_or_404(User, username=request.data['username'])
        
        if not user.check_password(request.data['password']):
            return Response({'errors': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UserSerializer(instance=user)
        date = datetime.datetime.now()
        payload = {
            'id': serializer.data['id'],
            'username': serializer.data['username'],
            'is_admin': '',#serializer.data[]
            'exp': date + datetime.timedelta(seconds=6000000),
            'iat': date,
        }
        print('Generated payload:', payload)
        token = jwt.encode(payload, SECRET_TOKEN_KEY, algorithm='HS256')
        print('Generated token:', token)
        
        response = Response(status=status.HTTP_200_OK)
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {'token': 'Is in cookies', 'user': serializer.data}
        
        return response

class LogoutView(APIView): #Hay que checar. Debería de quitarle el acceso a ese token. El usuario puede serguir obteniendo información
    
    def post(self, request):

        token = request.headers.get('Authorization', None)
        if not token:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        response = Response(status=status.HTTP_200_OK)
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

class UserView(APIView):
    def post(self, request):
        payload = get_user_from_token(request)
        
        user = User.objects.filter(id=payload['id']).first()
        if not user:
            raise AuthenticationFailed('User not found')
        
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserDeleteView(generics.DestroyAPIView):# Funcionando Correctamente
        
    def destroy(self, request, *args, **kwargs):
        payload = get_user_from_token(request)
        queryset = User.objects.filter(id=payload['id']).first()
        if queryset is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        self.perform_destroy(queryset)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
        
@api_view(['PUT', 'PATCH'])
def update_user_view(request):
    payload = get_user_from_token(request)
    user = User.objects.filter(id=payload['id']).first()
    serializer = UserUpdateSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# @api_view(['POST'])
# def staff(request):
#     payload = get_user_from_token(request)
#     staff = User.objects.filter(id=payload['id']).first()
#     if not staff.is_staff:
#         return Response(status=status.HTTP_401_UNAUTHORIZED)
    
#     users = []
#     for user in User.objects.all():
#         users.append(UserSerializer(instance = user).data)

#     #(request.user and request.user.is_staff)
#     return Response ({'users':users},status=status.HTTP_200_OK)


#Con Token puede -> Delete, Get 
#Sin Token -> Get, Post
class UsersViewSet(ModelViewSet): #Get y Post implemented
    
    serializer_class = UserSerializer
    update_serializer_class = UserUpdateSerializer
    # queryset = None
    
    def get_user_from_token(request):
        """Retorna Payload o Lanza un error"""
        #'Authorization':'Bearer jr23oifjn3pinv4938fuoeifj'
        auth_header = request.headers.get('Authorization', None)
        if auth_header is None:
            raise AuthenticationFailed('Authorization header missing')
        
        token = auth_header.split(' ')[1]
        if not token:
            raise AuthenticationFailed('Token missing')
            
        try:
            payload = jwt.decode(token, SECRET_TOKEN_KEY, algorithms=['HS256'])
            print('Decoded payload:', payload)
            return payload
        except jwt.ExpiredSignatureError:
            print('Token has expired')
            raise AuthenticationFailed('Token has expired') #400
        except jwt.JWTError as e:
            print('Invalid token error:', str(e))
            raise AuthenticationFailed('Invalid token') #407
    
    def get_queryset(self):
        return self.serializer_class().Meta.model.objects.all()
    
    def create_user_token(self, serializer) -> Response:
        """Add token in cookie. 
        Token data: id, username, expiration and iat."""
        payload = {
            'id' : serializer.data['id'],
            'username': serializer.data['username'],
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.now()
        }
        token = jwt.encode(payload, SECRET_TOKEN_KEY, algorithm='HS256').encode('utf-8')
        
        response = Response(status=status.HTTP_201_CREATED) 
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {'token':'Is in cookies', 'user':serializer.data}
        
        return response
    
    def create (self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response({'detail':'Data not valid'},status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return self.create_user_token(serializer)

    def list(self, request): 
        auth_header = request.headers.get('Authorization', None)
        if auth_header:
            payload = get_user_from_token(request)
            instance = User.objects.filter(id=payload['id']).first()
            
            return Response({'user':self.serializer_class(instance).data},status=status.HTTP_200_OK)
        
        #SOLO DEBERÍA DE PODER VER EL LISTADO DE USUSARIOS SI ES STAFF
        users_serializer = self.serializer_class(self.get_queryset(), many = True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        payload = get_user_from_token(request)
        
        queryset = User.objects.filter(id=payload['id']).first()
        if queryset is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        self.perform_destroy(queryset)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
       
    
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import viewsets
    

@api_view(['POST'])
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
    
    return response
    

@api_view(['POST'])
def login(request):
    print(f'{request.data['username'] = }')
    user = get_object_or_404(User, username=request.data['username'])
    
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

class UserProfileView(viewsets.GenericViewSet): #Visualiza sus datos y Puede modificarlos.
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):        
        return Response({'user': request.user.username}, status.HTTP_200_OK)
    
    def put(self, request):    
        serializer = UserUpdateSerializer(request.user, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        user = request.user
        user.delete()
        return Response({'detail': 'User deleted'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def staff(request):
    payload = get_user_from_token(request)
    staff = User.objects.filter(id=payload['id']).first()
    if not staff.is_staff:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    users = []
    for user in User.objects.all():
        users.append(UserSerializer(instance = user).data)

    #(request.user and request.user.is_staff)
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
