from django.urls import path
from .views import CreateView

urlpatterns = [
    path('', CreateView.as_view(), name='create'),
]
