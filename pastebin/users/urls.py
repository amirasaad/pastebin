from rest_framework.routers import DefaultRouter

from pastebin.users import viewsets

app_name = "users"

users_router = DefaultRouter()

users_router.register(r"users", viewsets.UsersViewSet)
