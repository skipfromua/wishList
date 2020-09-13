from rest_framework import permissions
from .models import Wishlist


class AuthorPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

