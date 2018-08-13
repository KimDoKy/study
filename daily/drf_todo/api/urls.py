from django.urls import path, include
from .views import TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', TodoViewSet, base_name='todos')
urlpatterns = router.urls
urlpatterns += [
    path('rest-auth/', include('rest_auth.urls')),
    ]
