from rest_framework.permissions import BasePermission
from .models import Post

class IsAuthor(BasePermission):

    def has_objects_permission(self, request, view, obj):
        if isinstance(Post, obj):
            return obj.author == request.user
        return obj.author == request.user
