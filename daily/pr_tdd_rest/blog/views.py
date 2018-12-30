from rest_framework import generics
from rest_framework import permissions

from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthor
from .models import Post

from django.contrib.auth.models import User

class CreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, IsAuthor)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, IsAuthor)

class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
