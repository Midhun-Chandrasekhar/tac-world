from functools import wraps
from flask import request
from flask_socketio import disconnect

from models.user import User
from utils import response_handler
from utils.response_codes import Messages, StatusCode


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_name = request.headers.get('user', None)
        user = User.objects(user_name=user_name).first()
        # TODO: Implement Token Authentication
        if not user:
            return response_handler.error(status=StatusCode.un_authorised, message=Messages.un_authorised)
        return f(*args, **kwargs)

    return decorated_function


def sock_auth(function):
    def user_auth(*args, **kwargs):
        user_name = request.headers.get('user', None)
        user = User.objects(user_name=user_name).first()
        # TODO: Implement Token Authentication
        if not user:
            disconnect()
            return
        args[0].user = user
        function(*args)
    return user_auth
