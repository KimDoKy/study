from rest_framework import serializers

from django.contrib.auth.models import User

from blog.models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'content', 'photo', 'create_date', 'update_date')
        read_only_fields = ('create_date', 'update_date')
