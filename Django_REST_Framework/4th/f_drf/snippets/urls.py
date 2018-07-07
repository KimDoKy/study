from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<pk>/', views.UserDetail.as_view(), name='user-detail'),
    ])

urlpatterns += [
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    ]
