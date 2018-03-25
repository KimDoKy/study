from django.shortcuts import render
from .models import Photo, Album
from django.views.generic import ListView
from util.gps import get_gps

AlbumView = ListView.as_view(model=Album, template_name='album_list.html')
