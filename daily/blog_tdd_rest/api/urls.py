from django.urls import path
from .views import CreateView, DetailsView

urlpatterns = [
    path('', CreateView.as_view(), name='create'),
    path('<pk>/', DetailsView.as_view(), name='details'),
    ]
