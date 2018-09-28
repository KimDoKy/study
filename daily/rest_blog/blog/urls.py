from django.urls import path
from .views import post_list, post_detail, post_new, post_edit

urlpatterns = [
        path('', post_list, name='post_list'),
        path('new/', post_new, name='post_new'),
        path('<pk>/', post_detail, name='post_detail'),
        path('<pk>/edit/', post_edit, name='post_edit'),
        ]
