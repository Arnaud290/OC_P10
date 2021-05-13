"""
Permissions module
"""
from rest_framework import permissions
from .services_permissions import (
    get_contributors_project,
    permission_method
)


class IsAuthorProjectOrContributorReadOnly(permissions.BasePermission):
    """The author of the project can modify. Contributors can read."""
    def has_permission(self, request, view):
        return permission_method(request)


class IsAuthorObjectOrContributorReadOnly(permissions.BasePermission):
    """The Author of the object (issue, comment) can modify.
    Contributors of the corresponding project can read."""
    def has_object_permission(self, request, view, obj):
        return permission_method(request, obj)


class IsContributorList(permissions.BasePermission):
    """Project contributors have the right to modify"""
    def has_permission(self, request, view):
        return get_contributors_project(request)
