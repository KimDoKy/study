from django.shortcuts import render
from .models import Photo, Album
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from util.gps import get_gps
from django.conf import settings
from django.urls import reverse_lazy

AlbumView = ListView.as_view(model=Album, template_name='album_list.html')
PhotoView = DetailView.as_view(model=Photo)
class PhotoDetailView(DetailView):
    model = Album
    template_name = 'album/album_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photo_list'] = Photo.objects.filter(album_id=self.kwargs['pk'])
        context['api'] = settings.GOOGLE_API
        for instance in context['photo_list']:
            instance.lat, instance.lng = get_gps(instance.photo.path)
            instance.save()
        return context

DetailView = PhotoDetailView.as_view()

UpdateView = CreateView.as_view(model=Photo, fields='__all__')

class PhotoDeleteView(DeleteView):
    model = Photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = context['object'].album_id
        return context

    def get_success_url(self):
        qs = Photo.objects.filter(pk=self.kwargs['pk'])
        for q in qs:
            return reverse_lazy('album:album_detail', args=(q.album_id,))

        
DelView = PhotoDeleteView.as_view()
