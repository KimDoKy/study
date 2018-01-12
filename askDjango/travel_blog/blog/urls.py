# blog/urls.py
from django.urls import path
from . import views
from . import views_cbv

app_name = 'blog'

urlpatterns = [
    path('', views_cbv.post_list, name='post_list'),
    path('new/', views.post_new, name='post_new'),
    path('<pk>/', views_cbv.post_detail, name='post_detail'),
    path('<id>/edit/', views.post_edit, name='post_edit'),
]
