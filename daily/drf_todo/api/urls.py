from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListTodo.as_view()),
    path('<pk>/', views.DetailTodo.as_view()),
    ]
