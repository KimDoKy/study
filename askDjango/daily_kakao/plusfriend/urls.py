from django.urls import path
from . import views

app_name = 'plusfriend'
urlpatterns = [
    path('keyboard', views.on_init),
    path('friend', views.on_added),
    path('friend/(?P<user_key>[\w-]+)$', views.on_block),
    path('chat_toom/(?P<user_key>[\w-]+)$', views.on_leave),
    path('message', views.on_message),
]
