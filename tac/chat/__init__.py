from flask import request
from flask_socketio import Namespace, emit, join_room, leave_room

from models.chat import Message, Room
from utils.auth_modules import sock_auth
from utils.response_handler import socket_response


class ChatApp(Namespace):
    @sock_auth
    def on_connect(self):
        # TODO: Joining notification
        join_room(Room.name)

    @sock_auth
    def on_disconnect(self):
        # TODO: Left notification
        leave_room(Room.name)

    @sock_auth
    def on_message(self, msg):
        text = msg.get('text')
        if not text:
            return
        message = Message(user=self.user, text=text).save()
        message = {
            "text": message.text,
            "created_at": str(message.created_at),
            "sender": message.user.user_name
        }
        message = socket_response(message=message)
        emit('notify', message, to=Room.name)
