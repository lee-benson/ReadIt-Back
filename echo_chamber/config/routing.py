from django.urls import path

from echo_chamber.chats.consumers import ChatConsumer

websockets_urlpatterns = [path("", ChatConsumer.as_asgi())]