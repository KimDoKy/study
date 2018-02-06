from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('new/', views.post_new, name='post_new'),
    path('<pk>/del/', views.post_delete),
    path('<pk>/edit/', views.post_edit, name='post_edit'),
    path('<pk>/', views.post_detail, name='post_detail'),
    ]
