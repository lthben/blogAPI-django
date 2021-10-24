# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post
from .models import Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    # author = serializers.ReadOnlyField(source='user.username')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
