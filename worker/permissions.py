from rest_framework.permissions import BasePermission

from .models import Worker


class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        try:
            return bool(request.user and hasattr(request.user, 'worker'))
        except Worker.DoesNotExist:
            return False
