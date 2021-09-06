"""
Auther : Midhun Chandrasekhar
         Software Engineer
Date: September 2 2021
Place: Kerala, India
"""

from flask import Flask, render_template
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_socketio import SocketIO

from chat import ChatApp
from api.chat import chat_component
from api import user_component
from settings.conf import ServerConf, DBConf

# Application configurations
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = DBConf.mongo_conf
MongoEngine(app)
CORS(app)
# TODO: Centralised logger, Error Report Management
socket = SocketIO(app, message_queue=ServerConf.redis_url)
socket.init_app(app, cors_allowed_origins=ServerConf.cors_hosts)


# App routes
@app.route("/")
def index():
    return render_template('index.html')


app.register_blueprint(user_component, url_prefix='/users')
app.register_blueprint(chat_component, url_prefix='/chats')
socket.on_namespace(ChatApp('/'))

# Application Entry
if __name__ == '__main__':
    app.run(ServerConf.host, ServerConf.port, ServerConf.debug)
