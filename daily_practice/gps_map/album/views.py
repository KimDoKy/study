from django.shortcuts import render
from .models import Photo, Album
from django.views.generic import ListView, DetailView
from util.gps import get_gps

AlbumView = ListView.as_view(model=Album, template_name='album_list.html')

class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'album/photo_list.html'

PhotoView = DetailView.as_view(model=Album)
