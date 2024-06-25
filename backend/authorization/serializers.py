from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator 
from django.utils.translation import gettext_lazy as _

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'validators': [MinLengthValidator(8, message=_("La contraseña debe tener al menos 8 caracteres"))]},
            'is_staff': {'required': False}
        }
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)  # Call the base class's create method to get the user instance

        if password:
            user.set_password(password)  # Set the user's password
            user.save()

        return user
    
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id', 'username', 'email','password']
        read_only_fields = ['id', 'username']
        extra_kwargs = {
            'password': {'write_only': True},
        }
        
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        
        instance = super().update(instance, validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance
