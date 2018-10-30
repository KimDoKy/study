from django.urls import path, re_path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', PostLV.as_view(), name='index'),
    path('post/', PostLV.as_view(), name='post_list'),
    path('post/<slug>/', PostDV.as_view(), name='post_detail'),
    path('archive/', PostAV.as_view(), name='post_archive'),
    path('<int:year>/', PostYAV.as_view(), name='post_year_archive'),
    path('<int:year>/<month>/', PostMAV.as_view(), name='post_month_archive'),
    path('<int:year>/<month>/<day>/', PostDAV.as_view(), name='post_day_archive'),
    path('today/', PostTAV.as_view(), name='post_today_archive'),
    path('tag/', TagTV.as_view(), name='tag_cloud'),
    #path('tag/<pk>/', PostTOL.as_view(), name='tagged_object_list'),
    re_path('tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(), name='tagged_object_list'),
]
