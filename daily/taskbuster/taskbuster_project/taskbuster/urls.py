# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from .views import home, home_files

urlpatterns = [
    path('<filename>', home_files, name='home-files'),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    )

