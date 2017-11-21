"""
Consumers that will handle connections between the server and the client.
Are a counterpart of Django views

Any user connected to our server will be added to the users group and receive
messages from the server
"""
import json
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http


@channel_session_user_from_http
def ws_connect(message):
    Group('users').add(message.reply_channel)
    Group('users').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': True,
            })
        })


@channel_session_user
def ws_disconnect(message):
    Group('users').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': False,
            })
        })
    Group('users').discard(message.reply_channel)


def message_handler(message):
    print(message['text'])
