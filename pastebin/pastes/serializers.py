from rest_framework import serializers
from rest_framework.reverse import reverse_lazy

from pastebin.pastes import models


class PasteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Paste
        fields = [
            "id",
            "content",
            "created",
            "shared_with",
            "is_public",
            "owner",
            "language",
            "style",
            "linenos",
        ]
