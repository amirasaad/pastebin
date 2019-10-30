from rest_framework.routers import DefaultRouter

from pastebin.subscriptions.viewsets import SubscriptionsViewSet


subscriptions_router = DefaultRouter()
subscriptions_router.register(r'subscriptions', SubscriptionsViewSet, basename='subscription')
