from django.urls import path
from .views import AccountListView, SignUp


urlpatterns = [
        path('', AccountListView.as_view(), name='accountlist'),
        path('signup/', SignUp.as_view(), name='signup'),
        ]
