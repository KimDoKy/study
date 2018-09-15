from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView

urlpatterns = [
    path('bucketlists/', CreateView.as_view(), name='create'),
    path('bucketlist/<pk>/', DetailsView.as_view(), name='detail'),
    ]

urlpatterns += format_suffix_patterns(urlpatterns)
