from django.urls import path
from .views import CreateView

urlpatterns = [
    path('bucketlists/', CreateView.as_view(), name='create'),
    ]
