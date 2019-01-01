from django.urls import path
from .views import post_list, DetailView

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<pk>/', DetailView.as_view(), name='post_detail'),
    ]
