from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    
    author = serializers.ReadOnlyField(source='request.user')
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'content', 'created', 'modified')
