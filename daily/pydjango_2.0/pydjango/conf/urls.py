from django.contrib import admin
from django.urls import path, include
#from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookmark/', include('bookmark.urls', namespace='bookmark')),
    path('blog/', include('blog.urls', namespace='blog')),

    # CBV
    #path('bookmark/', ListView.as_view(model=Bookmark), name='index'),
    #path('bookmark/<pk>/', DetailView.as_view(model=Bookmark), name='detail'),
]
