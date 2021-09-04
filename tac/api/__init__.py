from flask import Blueprint, request, jsonify

from models.user import User
from settings.middleware import login_required
from utils import response_handler
from utils.response_codes import Messages

user_component = Blueprint('api', __name__)


@user_component.route('/login', methods=['POST'])
def login():
    user_name = request.json.get('user_name')
    if not user_name:
        return response_handler.error(message=Messages.invalid_data)
    user = User.objects(user_name=user_name).first()
    if user:
        data = {'api': user.user_name}
        return response_handler.success(data, message=Messages.login_success)
    else:
        user = User(user_name=user_name).save()
        data = {'api': user.user_name}
        return response_handler.success(data, message=Messages.acc_created)


@user_component.route('/')
@login_required
def users():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 30))
    user_list = User.objects.paginate(page=page, per_page=limit).items
    user_list = list(map((lambda user: user.user_name), user_list))
    return response_handler.success(user_list, message=Messages.user_list)
