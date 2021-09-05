"""
Server Configurations

TODO: Once the platform for deployment is confirmed
      Update the configuration to support multi environment
      deployment
"""

import os


class ServerConf:
    port = 8000
    host = "0.0.0.0"
    debug = False
    r_host = 'redis'
    r_port = 6379
    endpoint = "http://localhost:81/"
    test_url = "http://localhost:81/"
    redis_url = 'redis://{}:{}/0'.format(r_host, r_port)
    cors_hosts = "*"


class DBConf:
    db_name = 'tac_world'
    host = 'mongodb'
    port = 27017
    mongo_conf = {
        'db': db_name,
        'host': host,
        'port': port
    }
    uri = {
        'host': 'mongodb://{}/{}'.format(host, db_name)
    }
