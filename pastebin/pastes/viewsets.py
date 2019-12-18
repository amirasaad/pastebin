"""
Module: pastebin.pastes.viewsets

Contains API for pastes app.
"""
from rest_framework.decorators import action
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from pastebin.pastes import serializers
from pastebin.pastes.filters import PasteFilter
from pastebin.pastes.models import Paste
from pastebin.pastes.permissions import IsOwnerOrCreate


class PastesViewSet(ModelViewSet):
    """API endpoint for pastes.
    """

    queryset = Paste.objects.all()
    serializer_class = serializers.PasteSerializer
    permission_classes = [IsOwnerOrCreate]
    filterset_class = PasteFilter

    @action(detail=True, renderer_classes=[StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        paste = self.get_object()
        return Response(paste.highlighted)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(owner=self.request.user)
        else:
            serializer.save(owner=None, is_public=True)
