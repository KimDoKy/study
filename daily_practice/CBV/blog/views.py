from django.views.generic import ListView
from django.conf import settings
from .models import Post

post_list = ListView.as_view(model=Post)
