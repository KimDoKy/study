from django.urls import path
from .views import CreateView, DetailView, post_list, post_detail, post_new

urlpatterns = [
    path('api/', CreateView.as_view(), name='create'),
    path('api/<pk>/', DetailView.as_view(), name='detail'),
    path('new/', post_new, name='post_new'),
    path('', post_list, name='post_list'),
    path('<pk>/', post_detail, name='post_detail'),
    ]
