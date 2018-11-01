from django.urls import path
from .views import AccountListView


urlpatterns = [
        path('', AccountListView.as_view(), name='accountlist'),
        ]
