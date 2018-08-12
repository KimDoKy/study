from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'blog'

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'uesrs', views.UserViewSet)

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('new/', views.post_new, name='post_new'),
    path('<pk>/', views.post_detail, name='post_detail'),
    path('<pk>/edit/', views.post_update, name='post_update'),
    path('<pk>/del/', views.post_del, name='post_del'),
    ]
