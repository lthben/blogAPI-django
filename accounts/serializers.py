# accounts.serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
