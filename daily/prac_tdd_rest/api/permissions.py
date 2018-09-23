from rest_framework.permissions import BasePermission
from .models import Todo

class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Todo):
            return obj.owner == request.user
        return obj.owner == reqest.user
