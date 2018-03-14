from .models import Post
from django.views.generic import ListView, DetailView, CreateView

post_list = ListView.as_view(model=Post)

post_detail = DetailView.as_view(model=Post)

post_new = CreateView.as_view(model=Post, fields='__all__')
