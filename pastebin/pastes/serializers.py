from rest_framework import serializers

from pastebin.pastes import models


class PasteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Paste
        fields = ['content', 'created', 'shared_with', 'is_public']
