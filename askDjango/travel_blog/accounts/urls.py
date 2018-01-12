from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.login, name='login',
         kwargs={
             'template_name': 'accounts/login_form.html',
             'authentication_form': LoginForm
         }),
    path('logout/', auth_views.logout, name='logout',
         kwargs={'next_page': settings.LOGIN_URL}),
    path('profile/', views.profile, name='profile'),
]
