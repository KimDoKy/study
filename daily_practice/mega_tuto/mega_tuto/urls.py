from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('page.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

]
