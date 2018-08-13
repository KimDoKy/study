from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'photo', 'author_id')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    author =  serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'author')
