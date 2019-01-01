from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

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
