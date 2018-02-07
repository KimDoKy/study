from django.urls import path
from .views import profile

app_name = 'account'

urlpatterns = [
    path('profile/', profile),
    ]
