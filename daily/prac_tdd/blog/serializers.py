from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'photo', 'author')
        read_only_fields = ('created', 'modified')
