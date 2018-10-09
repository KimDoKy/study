from django.urls import path
from .views import BookmarkLV, BookmarkDV

app_name = 'bookmark'

urlpatterns = [
    # CBV
    path('', BookmarkLV.as_view(), name='index'),
    path('<pk>/', BookmarkDV.as_view(), name='detail'),
]
