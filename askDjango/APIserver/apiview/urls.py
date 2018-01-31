from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'apiview'

router = DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'post', views.PostViewSet)

urlpatterns = [
	path('', include(router.urls)),
]
