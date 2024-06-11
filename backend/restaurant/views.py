from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer, MenuSerializer, TableSerializer, ReservationMenuSerializer, ReservationSerializer, ReservationStateSerializer
from .models import Menu, Reservation, ReservationMenu, ReservationState, Table, User

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] # o IsAuthenticated
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] # o IsAuthenticated
    
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
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [AllowAny]
    
class ReservationMenuViewSet(viewsets.ModelViewSet):
    queryset = ReservationMenu.objects.all()
    serializer_class = ReservationMenuSerializer
    permission_classes = [AllowAny] # [IsAuthenticated]