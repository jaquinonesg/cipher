from rest_framework import serializers
from .models import User

class UserSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'sip_authorization_name',
            'sip_authorization_password',
        ]    


class UserSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'ciphered_name',
            'ciphered_password'
        ]