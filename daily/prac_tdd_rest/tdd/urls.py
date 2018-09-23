from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('api.urls')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('get-token/', obtain_auth_token),
]
