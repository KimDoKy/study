from django.shortcuts import render
from .models import Post

def post_list(request):
    ps = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':qs})
