"""
ASGI config for booking_system project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import bookings.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'booking_system.settings')

application = get_asgi_application()


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'booking_system.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            bookings.routing.websocket_urlpatterns
        )
    ),
})