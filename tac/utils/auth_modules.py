from flask import request
from flask_socketio import disconnect

from models.user import User
from utils import response_handler
from utils.response_codes import StatusCode, Messages


def get_user():
    user_name = request.headers.get('user', None)
    user = User.objects(user_name=user_name).first()
    return user


def login_required(function):
    def user_auth(*args, **kwargs):
        # TODO: Implement Token Authentication
        if not get_user():
            return response_handler.error(status=StatusCode.un_authorised, message=Messages.un_authorised)
        return function(*args, **kwargs)
    return user_auth


def sock_auth(function):
    def user_auth(*args, **kwargs):
        user = get_user()
        # TODO: Implement Token Authentication
        if not user:
            disconnect()
            return
        args[0].user = user
        return function(*args, **kwargs)
    return user_auth
