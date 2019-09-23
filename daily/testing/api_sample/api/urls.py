from django.urls import path
from .views import *

urlpatterns = [
    path('test1/', test1),
    path('test2/', test2),
    path('test3/', test3),
    ]
