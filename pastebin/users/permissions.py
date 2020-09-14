from rest_framework.permissions import SAFE_METHODS, IsAuthenticated


class IsAuthenticatedOrCreate(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj == request.user
