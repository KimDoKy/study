from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    qs = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':qs})

def post_detail(request, pk):
    qs = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':qs})

def post_new(request):
    if request.method == 'POST':
        forms = PostForm(request.POST, request.FILES)
        if forms.is_valid():
            post = forms.save()
            return redirect(post)
    else:
        forms = PostForm()
    return render(request, 'blog/post_form.html', {'forms':forms})
