from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author', 'photo', 'date_created', 'date_modified')
        read_only_fields = ('date_creatd', 'date_modified')

class UserSerializer(serializers.ModelSerializer):
    
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'posts')
