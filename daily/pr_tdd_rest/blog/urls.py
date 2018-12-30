from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

from .views import CreateView, DetailView, UserView, UserDetailView

urlpatterns = {
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('posts/', CreateView.as_view(), name='create'),
    path('posts/<pk>/', DetailView.as_view(), name='details'),
    path('users/', UserView.as_view(), name='users'),
    path('users/<pk>/', UserDetailView().as_view(), name='user_details'),
    path('get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)
