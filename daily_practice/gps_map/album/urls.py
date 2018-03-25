from django.urls import path
from . import views

app_name = 'album'

urlpatterns = [
    path('', views.AlbumView, name='album_list'),
    path('new/', views.UpdateView, name='new_photo'),
    path('<pk>/', views.PhotoView, name='photo_detail'),
    ]
