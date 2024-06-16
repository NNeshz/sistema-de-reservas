from rest_framework import serializers
from django.contrib.auth.models import User

#Los serializers sirven para interpretar los Json y trabajarlos como Diccionarios

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id', 'username', 'email','password']
    
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