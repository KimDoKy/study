from django import forms
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Post

post_list = ListView.as_view(model=Post, paginate_by=3)

post_detail = DetailView.as_view(model=Post)

post_new = CreateView.as_view(model=Post)

post_edit = UpdateView.as_view(model=Post, fields='__all__')
