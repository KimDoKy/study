from django.urls import path
from .views import CreateView, DetailView

urlpatterns = [
    path('', CreateView.as_view(), name='create'),
    path('<pk>/', DetailView.as_view(), name='detail'),
]
