from django.urls import path
from .views import AccountListView, SignUp


urlpatterns = [
        path('', AccountListView.as_view(), name='accountlist'),
        path('sighup/', SignUp.as_view(), name='signup'),
        ]
