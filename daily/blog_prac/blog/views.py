from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from .forms import PostForm


class CreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

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
            return redirect('post_detail', post.id)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form':form})

def post_edit(request, pk):
    qs = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=qs)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', post.id)
    else:
        form = PostForm(instance=qs)
    return render(request, 'blog/post_form.html', {'form':form})

def post_del(request, pk):
    qs = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        qs.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm.html', {'post':qs})
