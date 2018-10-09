from django.contrib import admin
from django.urls import path
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

urlpatterns = [
    path('admin/', admin.site.urls),

    # CBV
    path('bookmark/', ListView.as_view(model=Bookmark), name='index'),
    path('bookmark/<pk>/', DetailView.as_view(model=Bookmark), name='detail'),
]
