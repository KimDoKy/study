from django.contrib import admin
from django.urls import path, include
from .drf_urls import *

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),

    # API document generation with drf_yasg
    path('v1/swagger<format>.json|.yaml/', schema_view_v1.without_ui(cache_timeout=0), name='schema-json'),
    path('v1/swagger/', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('v1/redoc/', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
    path('v2/redoc/', schema_view_v2.with_ui('redoc', cache_timeout=0), name='schema-redoc-v2'),
    path('v2/swagger<format>.json|.yaml/', schema_view_v2.without_ui(cache_timeout=0), name='schema-json'),
    path('v2/swagger/', schema_view_v2.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
