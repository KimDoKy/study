from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('edit/', views.post_new),
    path('<pk>/', views.post_detail, name='post_detail'),
    ]
