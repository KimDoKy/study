from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.conf.urls import include


urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<pk>/', views.UserDetail.as_view()),
    path('snippets/', views.SnippetList.as_view()),
    path('snipptes/<pk>/', views.SnippetDetail.as_view()),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    ]
