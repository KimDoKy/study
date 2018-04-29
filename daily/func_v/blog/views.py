from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q')
    if q:
        qs = qs.filter(title__icontains = q)
    return render(request, 'blog/post_list.html', {'posts':qs})


def post_detail(request, pk):
    qs = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':qs})
