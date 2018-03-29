from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post


post_list = ListView.as_view(model=Post)

post_detail = DetailView.as_view(model=Post)

post_new = CreateView.as_view(model=Post, fields='__all__')

post_edit = UpdateView.as_view(model=Post, fields='__all__')
