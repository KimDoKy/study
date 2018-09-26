from django.urls import path
from .views import post_list, post_detail, post_new

urlpatterns = [
    path('', post_list, name='post_list'),
    path('new/', post_new, name='post_new'),
    path('<pk>/', post_detail, name='post_detail'),
    ]
