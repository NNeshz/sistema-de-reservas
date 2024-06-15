from rest_framework.permissions import BasePermission

class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
    
class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Permitir métodos GET para cualquier usuario
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Permitir otros métodos solo para administradores
        return request.user and request.user.is_staff