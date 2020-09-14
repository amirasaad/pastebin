from rest_framework import serializers

from pastebin.subscriptions.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    stripe_token = serializers.CharField(write_only=True)

    class Meta:
        model = Subscription
        fields = ["id", "stripe_token"]
