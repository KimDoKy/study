from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'sample'

router = DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
	path('', include(router.urls)),
	]
