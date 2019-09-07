from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from drf_yasg import openapi

schema_url_v1_patterns = [
    path('v1/', include('blog.urls', namespace='sample')),
    path('v2/', include('blog.urls', namespace='sample')),
    ]

schema_view_v1 = get_schema_view(
        openapi.Info(
            title="Auto write docu test / blog",
            default_version='v1',
            description="api 문서 자동화 테스트입니다.",
            contact=openapi.Contact(email="makingfnuk0@gmail.com"),
            license=openapi.License(name="makingfunk comp"),
            ),
        validators = ['flex'],
        public=True,
        permission_classes=(AllowAny,),
        patterns=schema_url_v1_patterns,
        )

schema_view_v2 = get_schema_view(
        openapi.Info(
            title="Auto write docu test / version 2",
            default_version='v1',
            description="api 문서 자동화 version 2 테스트입니다.",
            contact=openapi.Contact(email="makingfnuk0@gmail.com"),
            license=openapi.License(name="makingfunk comp"),
            ),
        validators = ['flex'],
        public=True,
        permission_classes=(AllowAny,),
        patterns=schema_url_v1_patterns,
        )

