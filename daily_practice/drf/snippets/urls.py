from django.urls import path
from . import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<pk>/', views.snippet_detail),
]
