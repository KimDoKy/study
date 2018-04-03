from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers
from django.conf.urls import include

snippet_list = SnippetViewSet.as_view({
        'get': 'list',
        'post': 'create'
        })
snippet_detail = SnippetViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destory'
        })
snippet_highlight = SnippetViewSet.as_view({
        'get': 'highlight'},
        renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
        'get': 'list'
        })
user_detail = UserViewSet.as_view({
        'get': 'retrieve'
        })

urlpatterns = format_suffix_patterns([
        path('', api_root),
        path('snippets/', snippet_list, name='snippet-list'),
        path('snippets/<pk>/', snippet_detail, name='snippet-detail'),
        path('snippets/<pk>/highlight/', snippet_highlight, name='snippet-highlight'),
        path('user/', user_list, name='user-list'),
        path('user/<pk>/', user_detail, name='user-detail'),
        ])

urlpatterns += [
    path('api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    ]
