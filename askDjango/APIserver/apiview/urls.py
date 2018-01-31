from django.urls import path
from . import views

app_name = 'apiview'

urlpatterns = [
    path('post/', views.PostListAPIView.as_view()),
# path('post/', views.post_list),
    path('post/<pk>/', views.PostDetailAPIView.as_view()),
# path('post/<pk>/', views.post_detail),
]
