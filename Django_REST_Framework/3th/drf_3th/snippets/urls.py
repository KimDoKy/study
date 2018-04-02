from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snipptes/<pk>/', views.snippet_detail),
    ]
