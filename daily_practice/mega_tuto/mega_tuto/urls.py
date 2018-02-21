from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('page.urls')),

    # User management
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),

    # django admin
    path('admin/', admin.site.urls),

]
