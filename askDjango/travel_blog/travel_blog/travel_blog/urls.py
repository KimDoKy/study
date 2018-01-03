from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def root(request):
    return redirect('blog:post_list')

urlpatterns = [
    path('', root, name='root'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [ path('__debug__', include(debug_toolbar.urls)), ]

