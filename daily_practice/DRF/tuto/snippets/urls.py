from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf.urls import include

from .views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers

snippet_list = SnippetViewSet.as_view({
        'get': 'list',
        'post': 'create',
        })
snippet_detail = SnippetViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
        })
snippet_highlight = SnippetViewSet.as_view({
        'get': 'highlight'}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
        'get': 'list'
        })
user_detail = UserViewSet.as_view({
        'get': 'retrieve'
        })

urlpatterns = [
    path('', views.api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<pk>/', user_detail, name='user-detail'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    ]
