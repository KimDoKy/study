from .models import Post
from django.views.generic import ListView, DetailView

post_list = ListView.as_view(model=Post)

post_detail = DetailView.as_view(model=Post)
