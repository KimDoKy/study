from rest_framework import generics

from .serializers import PostSerializer
from .models import Post

from django.contrib.auth.models import User
class CreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save()
