from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser


class OwnerPermisson(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_anonymous():
            return False
        if request.user.is_staff:
            return True
        if obj and request.user == obj.user_created:
            return True
        return False