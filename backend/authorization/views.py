from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, UserUpdateSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication

#CRUD user + Login + Logout

@api_view(['POST'])
def register(request): 
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(): #Si la información recibida es válida (Contiene todos los campos requeridos, etc)
        serializer.save()
    
        user = User.objects.get(username=serializer.data['username']) #Obtengo el usuario comparando nombre de usuario
        user.set_password(serializer.data['password'])
        user.save() #Guardo el usuario
        
        token = Token.objects.create(user=user) #Genero el token
        
        response = Response({'user': serializer.data}, status.HTTP_201_CREATED)
        
        response.set_cookie( #Cookie retornada
            key='token',
            value=token.key,
            httponly=True,  # Asegura que la cookie no sea accesible vía JavaScript
            max_age=3600    # Tiempo en seg para que expire
        )
        return response
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    
    if not user.check_password(request.data['password']): #Sirve para comparar un string con un string ya encriptado
        return Response({'errors':'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)

    serializer = UserSerializer(instance=user)
    
    response = Response({'user': serializer.data}, status.HTTP_200_OK)
    
    response.set_cookie( #Cookie retornada
        key='token',
        value=token.key,
        httponly=True,  # Asegura que la cookie no sea accesible vía JavaScript
        max_age=3600    # Tiempo en seg para que expire
    )
    return response

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout (request):
    request.user.auth_token.delete()  #Quizás también debería de borrar la cookie
    return Response({'detail':'logout'}, status=status.HTTP_200_OK)

@api_view(['POST', 'GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    # print(str(get_authorization_header(request)))

    return Response({'user': request.user.username}, status.HTTP_200_OK)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_user(request):
    user = request.user
    user.delete()
    return Response({'detail': 'User deleted'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_user(request):
    user = request.user
    serializer = UserUpdateSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def staff(request):
    users = []
    for u in User.objects.all():
        users.append(UserSerializer(instance = u).data)

    #(request.user and request.user.is_staff)
    return Response ({'users':users}, status=status.HTTP_200_OK)

