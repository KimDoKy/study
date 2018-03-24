from django.contrib import admin
from .models import Photo, Album

class PhotoInline(admin.TabularInline):
    model = Photo

class AlbumAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline,
        ]

admin.site.register(Photo)
admin.site.register(Album, AlbumAdmin)
