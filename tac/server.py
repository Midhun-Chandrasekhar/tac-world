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

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = DBConf.mongo_conf
db = MongoEngine(app)
CORS(app)
socket = SocketIO(app)


@app.route("/")
def index():
    return render_template('index.html')


app.register_blueprint(user_component, url_prefix='/user')
app.register_blueprint(chat_component, url_prefix='/chat')
socket.on_namespace(ChatApp('/'))

if __name__ == '__main__':
    app.run(ServerConf.host, ServerConf.port, ServerConf.debug)
    socket = SocketIO(app, message_queue=ServerConf.redis_url)
