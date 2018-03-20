from .models import TestModel
from django.views.generic import ListView
from .gps import get_gps
from django.shortcuts import render

def test_view(request):
    qs = TestModel.objects.all()
    for instance in qs:
        try:
            photo_path = instance.photo.path
            instance.lat, instance.lng = get_gps(photo_path)
            instance.save()
        except KeyError as e:
            print(instance.id, e)
        except ValueError as e:
            print(instance.id, e)
    return render(request, 'testmodel/testmodel_list.html', {
            'testmodel_list':qs,
            })
    
