from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Menu, Reservation, ReservationMenu, ReservationState, Table, User

class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'is_staff']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff': {'required': False}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff': {'required': False}
        }

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        return super().update(instance, validated_data)
    
class TableSerializer(ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'chairs', 'price', 'description']

class ReservationStateSerializer(ModelSerializer):
    class Meta:
        model = ReservationState
        fields = ['id', 'state']

class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'description', 'price']

class ReservationSerializer(ModelSerializer):
    user   = PrimaryKeyRelatedField(queryset=User.objects.all())
    tables = PrimaryKeyRelatedField(queryset=Table.objects.all(), many=True)
    state  = PrimaryKeyRelatedField(queryset=ReservationState.objects.all())

    class Meta:
        model = Reservation
        fields = ['id', 'user', 'tables', 'start_date', 'end_date', 'state', 'created_at']

    def create(self, validated_data):
        tables_data = validated_data.pop('tables')
        reservation = Reservation.objects.create(**validated_data)
        reservation.tables.set(tables_data)
        return reservation
    
class ReservationMenuSerializer(ModelSerializer):
    # reservation = ReservationSerializer()
    # menu = MenuSerializer()

    class Meta:
        model = ReservationMenu
        fields = ['id', 'reservation', 'menu', 'amount']