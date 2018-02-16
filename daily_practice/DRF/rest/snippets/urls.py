from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'snippets'

urlpatterns = [
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<pk>/highlight/', views.SnippetHighlight.as_view()),
    path('snippets/<pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    ]
