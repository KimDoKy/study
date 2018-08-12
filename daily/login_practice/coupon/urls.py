from django.urls import path
from . import views

app_name = 'coupon'

urlpatterns = [
    path('', views.coupon_list, name='coupon_list'),
    ]
