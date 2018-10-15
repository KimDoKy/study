from django.contrib import admin
from django.urls import path, include
from bookmark.models import Bookmark
from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('bookmark/', include('bookmark.urls', namespace='bookmark')),
    path('blog/', include('blog.urls', namespace='blog')),

    # CBV
    #path('bookmark/', ListView.as_view(model=Bookmark), name='index'),
    #path('bookmark/<pk>/', DetailView.as_view(model=Bookmark), name='detail'),
]
