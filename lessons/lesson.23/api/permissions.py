from rest_framework import permissions


class OnlyForOneUser(permissions.IsAuthenticated):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        user = request.user
        print('USER', user)
        return user.username == 'user'
