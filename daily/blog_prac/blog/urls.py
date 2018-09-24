from django.urls import path
from .views import CreateView, DetailView, post_list, post_detail, post_new, post_edit, post_del

urlpatterns = [
    path('api/', CreateView.as_view(), name='create'),
    path('api/<pk>/', DetailView.as_view(), name='detail'),
    path('new/', post_new, name='post_new'),
    path('', post_list, name='post_list'),
    path('<pk>/', post_detail, name='post_detail'),
    path('<pk>/edit/', post_edit, name='post_edit'),
    path('<pk>/del/', post_del, name='post_del'),
    ]
