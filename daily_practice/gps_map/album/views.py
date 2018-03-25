from django.shortcuts import render
from .models import Photo, Album
from django.views.generic import ListView, DetailView
from util.gps import get_gps

AlbumView = ListView.as_view(model=Album, template_name='album_list.html')

class PhotoDetailView(DetailView):
    model = Album
    template_name = 'album/album_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photo_list'] = Photo.objects.filter(album_id=self.kwargs['pk'])
        for instance in context['photo_list']:
            instance.lat, instance.lng = get_gps(instance.photo.path)
            instance.save()
        return context

PhotoView = PhotoDetailView.as_view()
