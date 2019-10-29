from rest_framework.routers import DefaultRouter

from pastebin.pastes import viewsets

pastes_router = DefaultRouter()
pastes_router.register(r'pastes', viewsets.PastesViewSet)
