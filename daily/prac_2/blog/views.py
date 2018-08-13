from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets
from blog.serializers import PostSerializer, UserSerializer
from .models import Post

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def post_list(request):
    q = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':q})

def post_detail(request, pk):
    q = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':q})
