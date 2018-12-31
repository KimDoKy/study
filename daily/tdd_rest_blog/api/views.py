from django.shortcuts import render

from rest_framework import generics
from rest_framework import permissions

from .permissions import IsOwner
from .serializers import PostSerializer

from blog.models import Post

class CreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwner, permissions.IsAuthenticated)
