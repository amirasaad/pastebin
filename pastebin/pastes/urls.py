from rest_framework.routers import DefaultRouter

from pastebin.pastes import viewsets

app_name = "pastes"
pastes_router = DefaultRouter()
pastes_router.register(r"pastes", viewsets.PastesViewSet)
