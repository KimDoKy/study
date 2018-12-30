# api urls
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import CreateView, DetailView

urlpatterns = [
    path('posts/', CreateView.as_view(), name='create'),
    path('posts/<pk>/', DetailView.as_view(), name='details'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
