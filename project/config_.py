__author__ = 'Alessio'

import os

path_ = os.path.abspath(os.path.dirname(__file__))
path_testing = os.path.dirname(path_)


# value
DATABASE = "METER.LOG"
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'my_secret1'
CSRF_ENABLED = True

DEBUG = True
DATABASE_CONFIG_ = "Database\config.json"
DATABASE_CONFIG_DB = "Database\icollect_.db"

DATABASE_PATH_ = os.path.join(path_,DATABASE)
DATABASE_PATH_CONFIG = os.path.join(path_,DATABASE_CONFIG_)
DATABASE_PATH_CONFIG_DB = os.path.join(path_, DATABASE_CONFIG_DB)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH_CONFIG_DB

# Email Configurations

MAIL_SERVER =  'smtp.live.com' # smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'alessiobino@hotmail.com'
MAIL_PASSWORD = ''
MAIL_DEFAULT_SENDER = 'Admin TripleNet-Energy ' + MAIL_USERNAME


if __name__ == '__main__':
 pass
