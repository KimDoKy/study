from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post


def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q')
    if q:
        qs = qs.filter(title__icontains=q)
    return render(request, 'blog/post_list.html', {'post_list':qs})

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

def post_edit(request, pk):
    qs = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        forms = PostForm(request.POST, request.FILES, instance=qs)
        if forms.is_valid():
            post = forms.save()
            return redirect(post)
    else:
        forms = PostForm(instance=qs)
    return render(request, 'blog/post_form.html', {'forms':forms})

def post_del(request, pk):
    qs = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        qs.delete()
        return redirect('blog:post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post':qs})
