from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Subscription(models.Model):
    """Stores Users' subscriptions."""

    user = models.ForeignKey(
        User, related_name="subscriptions", on_delete=models.CASCADE
    )
    strip_customer_id = models.CharField(max_length=100)
    strip_subscription_id = models.CharField(max_length=100)
