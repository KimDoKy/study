from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post

class UserNameField(serializers.RelatedField):
    def to_representation(self, value):
        user_name = value.username
        return '%s' % user_name

class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = UserNameField(read_only=True)
    class Meta:
        model = Post
        fields = ('title', 'content', 'photo', 'author')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    author =  serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'author')
