from django.contrib import admin
from django.urls import path, include
import lists.views as lists

urlpatterns = [
    path('', lists.home_page, name='home'),
    path('admin/', admin.site.urls),
    ]
