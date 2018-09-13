from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView


urlpatterns = [
    path('bucket/', CreateView.as_view(), name='create'),
    path('bucket/<pk>/', DetailsView.as_view(), name='details'),
    ]

urlpatterns += format_suffix_patterns(urlpatterns)
