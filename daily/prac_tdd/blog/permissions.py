from rest_framework.permissions import BasePermission
from .models import Post

class IsAuthor(BasePermission):

    def has_objetc_permission(self, request, obj, view):
        if instance:
            return obj.author == request.user
        return obj.author == request.user
