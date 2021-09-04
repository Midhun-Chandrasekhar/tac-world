"""
Server Configurations
"""
import os


class ServerConf:
    port = "8000"
    host = "0.0.0.0"
    debug = True
    endpoint = "http://localhost:8000"
    test_url = "http://localhost:8000"
    redis_url = 'redis://localhost:6379/0'


class AppConf:
    api = os.environ.get('API', False)
    chat = os.environ.get('CHAT', False)


class DBConf:
    db_name = 'tac_world'
    host = 'localhost'
    port = 27017
    mongo_conf = {
        'db': db_name,
        'host': host,
        'port': port
    }
    uri = {
        'host': 'mongodb://{}/{}'.format(host, db_name)
    }
