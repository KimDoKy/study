from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


# class PostViewSet(viewsets.ModelViewSet):
class PostList(generics.ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
