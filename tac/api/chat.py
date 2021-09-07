from flask import Blueprint, request

from models.chat import Message
from utils import response_handler
from utils.auth_modules import login_required
from utils.constants import HISTORY_LENGTH, DEFAULT_PAGE
from utils.response_codes import Messages

chat_component = Blueprint('chat', __name__)


@chat_component.route('/')
@login_required
def chats():
    # TODO: Pagination helper Module
    page = int(request.args.get('page', DEFAULT_PAGE))
    limit = int(request.args.get('limit', HISTORY_LENGTH))
    msgs = Message.objects.order_by('-created_at').paginate(page=page, per_page=limit).items
    data = list(map((lambda msg: {
        "text": msg.text,
        "created_at": str(msg.created_at),
        "sender": msg.user.user_name
    }), msgs))
    data.reverse()
    return response_handler.success(data, message=Messages.chat_history)
