import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat import routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django_project.settings")

# Django ASGI application
django_asgi_app = get_asgi_application()

# Combined ASGI application
application = ProtocolTypeRouter({
    "http": django_asgi_app,  # Handles HTTP requests
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns  # WebSocket routing from chat app
        )
    ),
})