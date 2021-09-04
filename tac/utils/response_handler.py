import json

from flask import jsonify, make_response


def success(data=None, message=None):
    return make_response(jsonify({
        "status": "ok",
        "data": data,
        "message": message
    }), 200)


def error(status=400, message="Unknown_error"):
    return make_response(jsonify({
        "status": "err",
        "message": message
    }), status)


def socket_response(message_type="chat", message=None, info=None):
    return json.dumps({
        "message_type": message_type,
        "message": message,
        "info": info
    })