from django.contrib.auth.models import User
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.http import HttpResponse  
from rest_framework.views import APIView
from .serializers import (
    UserSerializer, 
    MenuSerializer, 
    TableSerializer, 
    ReservationMenuSerializer, 
    ReservationSerializer, 
    ReservationStateSerializer
)
from .models import Menu, Reservation, ReservationMenu, ReservationState, Table, User #InviteToken
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import IsStaff, IsStaffOrReadOnly

from django.contrib.auth import authenticate, login, logout
#La creación de usuarios parte del Staff se manejará a través de invitaciones en la casilla de notificaciones del usuario deseado. 
    #Esta función aún no está hecha

class CreateUserView(generics.CreateAPIView): #Se crea el usuario correctamente -> retorna token en cookie

    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    def perform_create(self, serializer): #Guarda usuario
        user = serializer.save()
        user.is_staff = False
        user.save()

    def create(self, request, *args, **kwargs): #Genera un respueta sin datos y una cookie con el token del user
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=request.data['username']) # Usa el usuario guardado
        
        response = Response({"detail": "The user was created successfully"}, status=status.HTTP_201_CREATED) #Datos retornados
        
        response.set_cookie( #Cookie retornada
            key='token',
            value=str(RefreshToken.for_user(user).access_token),
            httponly=True,  # Asegura que la cookie no sea accesible vía JavaScript
            max_age=3600    # Tiempo en seg para que expire
        )
        
        return response
      
class LogoutView(APIView): #Pendiente. El usuario puede 'deslogerse' de manera infinita. Ejectivamente elimina la cookie
    permission_classes = [IsAuthenticated]
  
    def post(self, request, *args, **kwargs):
  
        logout(request)
        response = Response({"detail": "Logged out successfully"}, status=status.HTTP_200_OK)
        
        response.delete_cookie('token')  # Elimina la cookie del token
    
        return response
    
class UserProfileView(generics.RetrieveAPIView):#Retorna datos de user y Token en cookie 

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user 
    
    def post(self, request, *args, **kwargs):
        # return request
        user = request.user
        serializer = self.get_serializer(user)
        response = Response(serializer.data, status=status.HTTP_200_OK)

        # Configura la cookie en la respuesta con un tiempo de expiración de 1 hora
        response.set_cookie(
            key='token',
            value=str(RefreshToken.for_user(user).access_token),
            httponly=True,  # Asegura que la cookie no sea accesible vía JavaScript
            max_age=3600    # Tiempo en segundos para que expire (1 hora)
        )

        return response

class LogginView(generics.GenericAPIView):#Retorna datos de user, Token en cookie y sessiónID 
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(request, username=username, password=password)
        if not (user is not None):
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        
        # Serializa los datos del usuario
        serializer = self.get_serializer(user)
        response = Response(serializer.data, status=status.HTTP_200_OK)

        refresh = RefreshToken.for_user(user)
        response.set_cookie(
            key='token',
            value=str(refresh.access_token),
            httponly=True,  # Asegura que la cookie no sea accesible vía JavaScript
            max_age=3600    # Tiempo en segundos para que expire (1 hora)
        )

        return response
    
class DeleteUserView(generics.DestroyAPIView):#Elimina correctamente al usuario
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user    

class UpdateUserView(generics.UpdateAPIView): #Actualiza los datos. No retorna token
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user   
    
    def perform_update(self, serializer):
        if not self.request.user.is_staff:
            serializer.save(is_staff=False)
        else:
            serializer.save()
        
class StaffOnlyView(generics.ListAPIView):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = UserSerializer
    permission_classes = [IsStaff]  
         
         
         
         
         
         
         
         
         
         
         
         
         
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsStaffOrReadOnly]
                    
class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsStaffOrReadOnly]

class ReservationStateViewSet(viewsets.ModelViewSet): 
    queryset = ReservationState.objects.all()
    serializer_class = ReservationStateSerializer
    permission_classes = [IsAuthenticated]
    
class ReservationViewSet(viewsets.ModelViewSet): #Devuelve reservaciones relacionadas con el usuario
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

    def perform_create(self, serializer): #Le asignamos la reserva recién creada al usuario
        serializer.save(user=self.request.user)
    
class ReservationMenuViewSet(viewsets.ModelViewSet): #Hay que arreglar el query set
    serializer_class = ReservationMenuSerializer
    permission_classes = [IsAuthenticated]
    
    

    def get_queryset(self):
        return ReservationMenu.objects.filter(id=self.request.user)
    
    
    
    
    
    
# class ProcessInviteView(generics.GenericAPIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, token, *args, **kwargs):
#         try:
#             invite_token = InviteToken.objects.get(token=token)
#             user = request.user

#             if user != invite_token.user:
#                 return Response({'error': 'Invalid token for this user'}, status=status.HTTP_400_BAD_REQUEST)

#             user.is_staff = True
#             user.save()
#             invite_token.delete()  # Eliminar el token después de su uso
#             return Response({'status': 'User promoted to staff'}, status=status.HTTP_200_OK)
        
#         except InviteToken.DoesNotExist:
#             return Response({'error': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)
    
    
    
# #Envío de Email de prueba. -> Funciona
# from django.conf import settings
# from django.core.mail import send_mail
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse
# @csrf_exempt
# def send_email(request):
#     user_email = 'user@example.com'  # Reemplaza esto con la lógica para obtener el correo del usuario.
#     send_mail(
#         'Hola',
#         '¿Cómo estás?',
#         settings.DEFAULT_FROM_EMAIL,
#         [user_email],
#         fail_silently=False,
#     )
#     return HttpResponse('Correo enviado.')


# #Necesario para testear el envío de correos. Al hacer una peticion get se obtiene X-CSRFToken header necesario
# from django.shortcuts import render
# def email_form(request):
#     return render(request, 'email_form.html')

