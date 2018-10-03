from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import PostForm
from .models import Post

def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q')
    print(q)
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
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(reverse('post_detail', kwargs={'pk':post.id}))
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form':form})

def post_edit(request, pk):
    qs = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=qs)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(reverse('post_detail', kwargs={'pk':qs.id}))
    else:
        form = PostForm(instance=qs)
    return render(request, 'blog/post_form.html', {'form':form})
