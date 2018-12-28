from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author', 'photo', 'date_created', 'date_modified')
        read_only_fields = ('date_creatd', 'date_modified')
