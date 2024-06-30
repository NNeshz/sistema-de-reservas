from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.contrib.auth.models import User

from .serializers import UserSerializer, CustomTokenObtainPairSerializer, UserUpdateSerializer

from rest_framework_simplejwt.views import TokenObtainPairView

from .models import InviteToken 

#CRUD user + Login + Logout + Staff Invitation

class SendStaffInvitationView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request): #El token está vinculado por lo que solo funcionará cuando el usuario deseado lo active

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

class ProcessStaffInvitationView(APIView):
    permission_classes = [IsAuthenticated]
    def get(request):
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

def get_custom_token(data:{'request.data'}) -> str:

    serializer = CustomTokenObtainPairSerializer(data={
        'username': data.get('username'),
        'password': data.get('password')
    })
    
    serializer.is_valid(raise_exception=True)
    
    return  serializer.validated_data #Token

def set_token (data:{'request.data'}, status=status.HTTP_200_OK) -> Response['Response.set_cookie("token")']:
    """
    data = request.data
    Response =Response.set_cookie("token")
    """
    response = Response(status=status)
    response.set_cookie('token', get_custom_token(data))
    return response

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    # permission_classes = (AllowAny, )
    
    def post (self, request):
        user = get_object_or_404(User, username=request.data['username'])
        
        if not user.check_password(request.data['password']):
            return Response({'errors': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
 
        return set_token(request.data)
    
class UsersListView(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    
    def get(self, request):
        self.queryset = User.objects.all()
        users = self.serializer_class(self.queryset, many=True)
        return Response({'users':users.data}, status=status.HTTP_200_OK)

class UserCreateView (APIView):
    serializer_class = UserSerializer

    def post(self,request):
        validated_data = self.serializer_class(data=request.data)
    
        if not validated_data.is_valid():
            return Response({'detail':('Data no valid',)},status=status.HTTP_400_BAD_REQUEST)
        
        User.objects.create_user(**validated_data.data)
        
        return set_token(request.data, status.HTTP_201_CREATED)
   
class UserProfileView (APIView): 
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    serializer_update_class = UserUpdateSerializer
    def put(self, request):
        user = request.user
        serializer = self.serializer_update_class(user, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        u = request.user
        return Response({'id':u.pk, 'username':u.username, 'email':u.email, 'is_staff':u.is_staff})
        
    def delete(self, request):
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
