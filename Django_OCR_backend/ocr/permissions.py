from rest_framework.permissions import IsAuthenticated, BasePermission

class AllowOptionsAuthentication(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'OPTIONS':
            return True
        return request.user and request.user.is_authenticated
