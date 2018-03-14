from django.views.generic import ListView, DetailView, CreateView
from django.conf import settings
from .models import Post

post_list = ListView.as_view(model=Post)

post_detail = DetailView.as_view(model=Post)

post_new = CreateView.as_view(model=Post, fields='__all__')
