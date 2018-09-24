from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


class CreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def post_list(request):
    post = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':post})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})
