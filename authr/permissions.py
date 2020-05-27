from rest_framework import permissions
from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404

def _has_permission_(user):
    """
     Revisa si el usuario de la petición tiene el permiso en cuestión
    """
    return user.has_perm('authr.view_user')

class IsAuthorized(permissions.BasePermission):
    message = 'El usuario no tiene permisos para acceder a este módulo.'
    def has_permission(self, request, view):
        # user = get_object_or_404(User, pk=1)
        # return _has_permission_(user)
        # return user.has_perm('plan.view_plan')
        return request.user.has_perm('authr.view_user')
        