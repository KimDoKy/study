from django.urls import path
from . import views

app_name = 'album'

urlpatterns = [
    path('', views.AlbumView, name='album_list'),
    path('new/', views.UpdateView, name='new_photo'),
    path('photo/<pk>/', views.PhotoView, name='photo'),
    path('<pk>/del/', views.DelView, name='photo_del'),
    path('<pk>/', views.DetailView, name='album_detail'),
    ]
