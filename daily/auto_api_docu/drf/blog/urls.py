from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('create/', views.CreateView.as_view(), name='create_view'),
    path('<pk>/', views.DetailView.as_view(), name='detail_view'),
    ]
