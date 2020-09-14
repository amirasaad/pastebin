import stripe
from django.conf import settings
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from pastebin.subscriptions.models import Subscription
from pastebin.subscriptions.serializers import SubscriptionSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY


class SubscriptionsViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):

    permission_classes = [IsAuthenticated]
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        return self.request.user.subscriptions.all()

    def perform_create(self, serializer):
        # Allow only one subscription
        user = self.request.user
        sup = Subscription.objects.filter(user=user).first()
        if sup is None:
            customer = stripe.Customer.create(
                email=user.email, source=self.request.POST["stripe_token"]
            )
            sub1 = stripe.Subscription.create(
                customer=customer.stripe_id, items=[{"plan": "prod_G5V5RMHcZ7bcbJ"}]
            )
            serializer.save(
                user=self.request.user,
                strip_customer_id=customer.stripe_id,
                strip_subscription_id=sub1.stripe_id,
            )
