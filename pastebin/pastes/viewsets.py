from rest_framework.viewsets import ModelViewSet

from pastebin.pastes.filters import PasteFilter
from pastebin.pastes.models import Paste
from pastebin.pastes import serializers
from pastebin.pastes.permissions import IsOwnerOrCreate


class PastesViewSet(ModelViewSet):
    queryset = Paste.objects.all()
    serializer_class = serializers.PasteSerializer
    permission_classes = [IsOwnerOrCreate]
    filterset_class = PasteFilter

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(owner=self.request.user)
        else:
            serializer.save(owner=None, is_public=True)
