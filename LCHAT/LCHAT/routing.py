"""
Work in a similar manner to Django URLs
"""
from channels.routing import route
from instant.consumers import ws_connect, ws_disconnect, message_handler

channel_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.disconnect', ws_disconnect),
    route('websocket.receive', message_handler),
    ]
