from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


post_list = ListView.as_view(model=Post, template_name='post_list.html')

post_detail = DetailView.as_view(model=Post, template_name='blog/post_detail.html')
