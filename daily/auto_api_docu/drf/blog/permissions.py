from rest_framework.permissions import BasePermission
from .models import Post


class IsAuthor(BasePermission):

    def has_object_permission(self, request, view, obj):
        if isinstance:
            return obj.author == request.user
        return obj.author == request.user
