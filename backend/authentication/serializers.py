from django.contrib.auth.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model  = User
        fields = ('id', 'username', 'password', 'email', 'is_staff')
        extra_kwargs = { 'password': {'write_only': True}, 'is_staff':{'read_only':True}, 'id':{'read_only':True}, }
                
    
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id', 'username', 'email','password']
        read_only_fields = ['id']
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

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Agrega datos adicionales al payload del token
        token['user_id'] = user.id
        token['username'] = user.username
        token['email'] = user.email
        token['is_staff'] = user.is_staff

        return token