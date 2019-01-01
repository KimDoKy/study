from django.urls import path
from .views import post_list, PostDetailView, PostCreateView

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('edit/', PostCreateView.as_view(), name='post_edit'),
    ]
