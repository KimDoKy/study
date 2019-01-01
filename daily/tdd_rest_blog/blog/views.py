from django.shortcuts import render

from .models import Post

def post_list(request):
    posts = Post.objects.all()
    q = request.GET.get('q')
    if q:
        posts = posts.filter(title__icontains=q)
    return render(request, 'blog/post_list.html', {'posts':posts})
