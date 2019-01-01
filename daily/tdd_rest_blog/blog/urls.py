from django.urls import path
from .views import post_list, PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('edit/', PostCreateView.as_view(), name='post_edit'),
    ]
