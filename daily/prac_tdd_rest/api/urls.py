from django.urls import path
from .views import CreateView, DetailView

urlpatterns = [
    path('bucketlists/', CreateView.as_view(), name='create'),
    path('bucketlists/<pk>/', DetailView.as_view(), name='detail'),
    ]
