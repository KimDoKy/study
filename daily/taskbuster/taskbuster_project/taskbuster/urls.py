from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import home, home_files

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('<filename>', home_files, name='home-files'),
#  url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
#            home_files, name='home-files'),
]
