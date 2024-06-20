from django.contrib.auth.models import User
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from ..serializers import (
    ReservationMenuSerializer, 
    ReservationSerializer, 
    ReservationStateSerializer
)
from ..models import Reservation, ReservationMenu, ReservationState, InviteToken
from ..permissions import IsStaff, IsStaffOrReadOnly
# from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view








#La creación de usuarios parte del Staff se manejará a través de invitaciones en la casilla de notificaciones del usuario deseado. 
    #Esta función aún no está hecha

#Debería crear otro serializer para las reservas. Uno solo debe poder leer estados y el otro modificarlos  
#Lo mismo para el tema de los precios en los platos y las reservas de menús
 
 
from rest_framework.exceptions import AuthenticationFailed
from ..admin import SECRET_TOKEN_KEY  
from jose import jwt
def get_user_from_token(request):
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
 
 
 
#Los estados deberían ser manejados por el Staff -> Los usuario solo pueden leer.
class ReservationStateViewSet(viewsets.ModelViewSet):
    queryset = ReservationState.objects.all()
    serializer_class = ReservationStateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStaffOrReadOnly]
            
class ReservationViewSet(viewsets.ModelViewSet): #Devuelve reservaciones relacionadas con el usuario
    serializer_class = ReservationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

    def perform_create(self, serializer): #Le asignamos la reserva recién creada al usuario
        serializer.save(user=self.request.user)
    
class ReservationMenuViewSet(viewsets.ModelViewSet): #Hay que arreglar el query set
    serializer_class = ReservationMenuSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return ReservationMenu.objects.filter(id=self.request.user)
    
@api_view(['POST'])
def ProcessInviteView(request):
    print('\n\n\n\n')
    try:
        payload = get_user_from_token(request)
        user = User.objects.filter(id=payload['id']).first()   
        invite_token = InviteToken.objects.create(payload['id'])
        
    #     print(invite_token)
    #     print(request, token)
    #     invite_token = InviteToken.objects.get(token=token)
    #     user = request.user

    #     if user != invite_token.user:
    #         return Response({'error': 'Invalid token for this user'}, status=status.HTTP_400_BAD_REQUEST)

    #     user.is_staff = True
    #     user.save()
    #     invite_token.delete()  # Eliminar el token después de su uso
    #     return Response({'status': 'User promoted to staff'}, status=status.HTTP_200_OK)
    
    except InviteToken.DoesNotExist:
        return Response({'error': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)
    

    
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

