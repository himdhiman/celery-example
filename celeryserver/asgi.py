import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from api.routing import ws_urlpatterns


from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryserver.settings')

application = ProtocolTypeRouter({
    "http" : get_asgi_application(),
    "websocket" : AuthMiddlewareStack(URLRouter(ws_urlpatterns)),
})
