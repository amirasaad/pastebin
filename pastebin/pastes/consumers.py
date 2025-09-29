from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json

from pastebin.pastes.serializers import PasteSerializer


class PastesConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        user = self.scope['user']
        print(user)
        await self.accept()

    async def receive_json(self, content, **kwargs):
        message_type = content.get('type')
        if message_type == 'create.paste':
            await self.create_paste(content)

    async def create_paste(self, event):
        paste = await self._create_paste(event.get('data'))
        paste_data = PasteSerializer(paste).data
        await self.send_json({
            'type': 'create.paste',
            'data': paste_data
        })

    @database_sync_to_async
    def _create_paste(self, content):
        serializer = PasteSerializer(data=content)
        serializer.is_valid(raise_exception=True)
        paste = serializer.create(serializer.validated_data)
        return paste
