from django.shortcuts import render

from rest_framework import generics

from .serializers import PostSerializer

from blog.models import Post

class CreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save()
