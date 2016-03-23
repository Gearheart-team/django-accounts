from rest_framework.permissions import BasePermission


# TODO: THIS IS WRONG!!!
# TODO: Instead, we need to allow
# * anonymous users to create
# * logged in users to view
# * only self or superuser to update/delete
class BaseUserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated() or request.method == 'POST'
