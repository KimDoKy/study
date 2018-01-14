from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.logout, name='logout',
         kwargs={'next_page': settings.LOGIN_URL}),
    path('profile/', views.profile, name='profile'),
]
