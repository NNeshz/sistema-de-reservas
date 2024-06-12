from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import CreateUserSerializer, UserSerializer, MenuSerializer, TableSerializer, ReservationMenuSerializer, ReservationSerializer, ReservationStateSerializer
from .models import Menu, Reservation, ReservationMenu, ReservationState, Table, User
from .permissions import IsStaff

class DeleteUserView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user    

class StaffOnlyView(generics.ListAPIView):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = UserSerializer
    permission_classes = [IsStaff]

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