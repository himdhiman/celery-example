from django.urls import path
from api import consumers

ws_urlpatterns = [
    path('ws/number/<int:id>/', consumers.NumberConsumer.as_asgi())
]