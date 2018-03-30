from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment


post_list = ListView.as_view(model=Post)

post_detail = DetailView.as_view(model=Post)

post_new = CreateView.as_view(model=Post, fields='__all__')

post_edit = UpdateView.as_view(model=Post, fields='__all__')

post_del = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:post_list'))

