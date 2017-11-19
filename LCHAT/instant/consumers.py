"""
Consumers that will handle connections between the server and the client.
Are a counterpart of Django views

Any user connected to our server will be added to the users group and receive
messages from the server
"""
from channels import Group


def ws_connect(message):
    Group('users').add(message.reply_channel)


def ws_disconnect(message):
    Group('users').discard(message.reply_channel)
