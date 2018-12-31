# api urls
from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns

from .views import CreateView, DetailView

urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('posts/', CreateView.as_view(), name='create'),
    path('posts/<pk>/', DetailView.as_view(), name='details'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
