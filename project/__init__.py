__author__ = 'Alessio'

import json
from datetime import datetime
import logging
import threading

from flask import Flask
from gevent import monkey
from gevent.pywsgi import WSGIServer
from flask_socketio import SocketIO
from gunicorn import *
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment

#from  import create_json_building, create_json_table, create_json_tne, create_tenant_building


#monkey.patch_all()


app = Flask(__name__)

# application moment for time e location
moment = Moment(app)


app.config.from_pyfile('config_.py')

# applications Socketio
socketio = SocketIO(app)


# database
db = SQLAlchemy(app)

from setting.view import blueprint_setting
from general.view import blueprint_general
from broker.view import blueprint_mqtt_data
from users.view import users_for_blueprint
from error.view import blueprints_error

#register
app.register_blueprint(blueprint_setting)
app.register_blueprint(blueprint_general)
app.register_blueprint(blueprint_mqtt_data)
app.register_blueprint(users_for_blueprint)
app.register_blueprint(blueprints_error)












