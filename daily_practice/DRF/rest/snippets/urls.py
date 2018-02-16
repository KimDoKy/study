from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'snippets'

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view(), name='snippet_list'),
    path('snippets/<pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    path('snippets/<pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<pk>/', views.UserDetail.as_view(), name='user-detail'),
])

urlpatterns += [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    ]
