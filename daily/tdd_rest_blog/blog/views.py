from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post

def post_list(request):
    posts = Post.objects.all()
    q = request.GET.get('q')
    if q:
        posts = posts.filter(title__icontains=q)
    return render(request, 'blog/post_list.html', {'posts':posts})

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title','author', 'content', 'photo']

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'author', 'content', 'photo']

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')
