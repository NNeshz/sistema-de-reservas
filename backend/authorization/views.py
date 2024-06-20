from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import generics
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




@api_view(['POST'])
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

