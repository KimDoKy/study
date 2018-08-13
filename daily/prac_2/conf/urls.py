from django.contrib import admin
from django.urls import path, include
from blog import views
from rest_framework.routers import DefaultRouter

app_name = 'blog'

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
