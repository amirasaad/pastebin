from rest_framework import permissions


class IsOwnerOrCreate(permissions.IsAuthenticated):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return (
                obj.is_public
                or request.user in obj.shared_with.all()
                or obj.owner == request.user
            )

        return obj.owner == request.user
