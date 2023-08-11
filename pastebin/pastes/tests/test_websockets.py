
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import Client
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer
from channels.testing import WebsocketCommunicator
import pytest

from config.routing import application
from pastebin.pastes.models import Paste


TEST_CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}


@database_sync_to_async
def create_user(
    *,
    username='user@example.com',
    password='pAssw0rd!',
):
    # Create user.
    user = get_user_model().objects.create_user(
        username=username,
        password=password
    )
    return user


async def auth_connect(user):
    # Force authentication to get session ID.
    client = Client()
    client.force_login(user=user)

    # Pass session ID in headers to authenticate.
    communicator = WebsocketCommunicator(
        application=application,
        path='ws/paste/',
        headers=[(
            b'cookie',
            f'sessionid={client.cookies["sessionid"].value}'.encode('ascii')
        )]
    )
    connected, _ = await communicator.connect()
    assert connected is True
    return communicator


async def connect_and_create_paste(
    *,
    user,
    content='Class A(): pass',
    language='python'
):
    communicator = await auth_connect(user)
    await communicator.send_json_to({
        'type': 'create.paste',
        'data': {
            'content': content,
            'language': language,
            'owner': user.id,
        }
    })
    return communicator


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
class TestWebsockets:

    async def test_authorized_user_can_connect(self, settings):
        # Use in-memory channel layers for testing.
        settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS

        user = await create_user(
            username='user@example.com'
        )
        communicator = await auth_connect(user)
        await communicator.disconnect()

    async def test_user_can_create_pastes(self, settings):
        settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS

        user = await create_user(
            username='user@example.com'
        )
        communicator = await connect_and_create_paste(user=user)

        # Receive JSON message from server.
        response = await communicator.receive_json_from()
        data = response.get('data')

        # Confirm data.
        assert data['id'] is not None
        assert 'Class A(): pass' == data['content']
        assert 'python' == data['language']
        assert user.id == data['owner']

        await communicator.disconnect()
