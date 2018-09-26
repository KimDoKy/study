from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('blog.urls')),
    path('api/', include('api.urls')),
    path('get-token/', obtain_auth_token),
]
