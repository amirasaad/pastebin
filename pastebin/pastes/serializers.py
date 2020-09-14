from rest_framework import serializers
from rest_framework.reverse import reverse_lazy

from pastebin.pastes import models


class PasteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    shortened_url = serializers.SerializerMethodField()

    class Meta:
        model = models.Paste
        fields = [
            "content",
            "created",
            "shared_with",
            "is_public",
            "owner",
            "shortened_url",
            "language",
            "style",
            "linenos",
        ]

    def get_shortened_url(self, obj):
        request = self.context["request"]
        return reverse_lazy(
            "pastes:paste-detail", kwargs={"version": 1, "pk": obj.pk}, request=request
        )
