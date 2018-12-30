# api urls
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import CreateView

urlpatterns = [
    path('posts/', CreateView.as_view(), name='create'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
