from django.urls import path
from . import views
from . import views_cbv

urlpatterns = [
    path('post_list1', views.post_list1),
    path('post_list2', views.post_list2),
    path('post_list3', views.post_list3),
    path('excel_down', views.excel_download),

    path('cbv/post_list1', views_cbv.post_list1),
]
