from django.urls import path
from .views import post_list, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'blog'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/del/', PostDeleteView.as_view(), name='post_del'),
    path('edit/', PostCreateView.as_view(), name='post_edit'),
    ]
