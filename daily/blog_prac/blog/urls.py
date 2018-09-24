from django.urls import path
from .views import CreateView, DetailView, post_list

urlpatterns = [
    path('api/', CreateView.as_view(), name='create'),
    path('api/<pk>/', DetailView.as_view(), name='detail'),
    path('', post_list, name='post_list'),
    ]
