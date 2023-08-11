from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

import pastebin.pastes.routing


application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            pastebin.pastes.routing.websocket_urlpatterns
        )
    ),
})
