from django.urls import path, include
from .views import CreateView, DetailView

urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', CreateView.as_view(), name='create'),
    path('<pk>/', DetailView.as_view(), name='detail'),
    ]
