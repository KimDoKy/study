from django.urls import path
from . import views

app_name = 'plusfriend'
urlpatterns = [
    path('keyboard', views.on_init),
    path('friend', views.on_added),
    path('friend/<user_key>', views.on_block),
    path('chat_toom/<user_key>', views.on_leave),
    path('message', views.on_message),
    path('diary/<user_key>/', views.post_list, name='post_list'),
]
