from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

from django.contrib.auth.models import User
from rest_framework import viewsets
from blog.serializers import PostSerializer, UserSerializer

def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q')
    if q:
        qs = qs.filter(title__icontains=q)
    return render(request, 'blog/post_list.html', {'posts':qs})

def post_detail(request, pk):
    qs = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':qs})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form':form})
    
def post_update(request, pk):
    qs = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=qs)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm(instance=qs)
    return render(request, 'blog/post_form.html', {'form':form})

def post_del(request, pk):
    qs = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        qs.delete()
        return redirect('blog:post_list')
    return render(request, 'blog/post_confirm.html', {'qs':qs})

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
