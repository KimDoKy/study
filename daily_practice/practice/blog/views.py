from .models import Post
from django.views.generic import ListView

post_list = ListView.as_view(model=Post)
