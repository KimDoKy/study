from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
	post = Post.objects.all()
	return render(request, 'blog/post_list.html', {'post_list':post})

def post_detail(request, pk):
	qs = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':qs})
