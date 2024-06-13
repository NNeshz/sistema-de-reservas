from django.contrib.auth.models import User
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    CreateUserSerializer, 
    UserSerializer, 
    MenuSerializer, 
    TableSerializer, 
    ReservationMenuSerializer, 
    ReservationSerializer, 
    ReservationStateSerializer
)
from .models import Menu, Reservation, ReservationMenu, ReservationState, Table, User, InviteToken
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import IsStaff

#Necesario para testear el envío de correos. Al hacer una peticion get se obtiene X-CSRFToken header necesario
from django.shortcuts import render
def email_form(request):
    return render(request, 'email_form.html')

#Envío de Email de prueba. -> Funciona
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

class ProcessInviteView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, token, *args, **kwargs):
        try:
            invite_token = InviteToken.objects.get(token=token)
            user = request.user

            if user != invite_token.user:
                return Response({'error': 'Invalid token for this user'}, status=status.HTTP_400_BAD_REQUEST)

            user.is_staff = True
            user.save()
            invite_token.delete()  # Eliminar el token después de su uso
            return Response({'status': 'User promoted to staff'}, status=status.HTTP_200_OK)
        
        except InviteToken.DoesNotExist:
            return Response({'error': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class DeleteUserView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user    

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]  # Permitir a cualquiera crear un usuario

    def perform_create(self, serializer):
        # Solo permitir a los usuarios autenticados y con permisos especiales crear usuarios del staff
        if self.request.user.is_authenticated and self.request.user.is_staff:
            serializer.save()
        else:
            serializer.save(is_staff=False)
        
class UpdateUserView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user   
    
    def perform_update(self, serializer):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            serializer.save()
        else:
            # No permitir que usuarios normales actualicen usuarios del staff
            serializer.save(is_staff=False)
   
class StaffOnlyView(generics.ListAPIView):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = UserSerializer
    permission_classes = [IsStaff]  
            
class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [AllowAny]

class ReservationStateViewSet(viewsets.ModelViewSet):
    queryset = ReservationState.objects.all()
    serializer_class = ReservationStateSerializer
    permission_classes = [AllowAny]
    
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [AllowAny]
    
class ReservationViewSet(viewsets.ModelViewSet):
    
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)
    
class ReservationMenuViewSet(viewsets.ModelViewSet):
    queryset = ReservationMenu.objects.all()
    serializer_class = ReservationMenuSerializer
    permission_classes = [AllowAny] # [IsAuthenticated]