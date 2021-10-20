# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    # author = serializers.ReadOnlyField(source='user.username')
