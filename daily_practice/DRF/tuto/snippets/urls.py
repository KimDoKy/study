from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.SnippetList.as_view()),
    path('<pk>/', views.SnippetDetail.as_view()),
    path('user/', views.UserList.as_view()),
    path('user/<pk>/', views.UserDetail.as_view()),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    ]
