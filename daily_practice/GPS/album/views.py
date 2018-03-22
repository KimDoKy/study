from django.shortcuts import render
from .models import Album
from util.gps import get_gps
from django.conf import settings


def photo_list(request):
    qs = Album.objects.all()
    api_key = settings.MAP_API
    for instance in qs:
        instance.lat, instance.lng = get_gps(instance.photo.path)
        instance.save()
    return render(request, 'album/photo_list.html', {
            'qs':qs,
            'api':api_key,
            })
            
