from django.contrib import admin
from django.urls import path, include
from account.views import KakaoLogin, NaverLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/kakao/', KakaoLogin.as_view(), name='kk_login'),
    path('rest-auth/naver/', NaverLogin.as_view(), name='nv_login'),
]
