__author__ = 'Alessio'

import os

path_ = os.path.abspath(os.path.dirname(__file__))

# value
DATABASE = "METER.LOG"
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'my_secret'
CSRF_ENABLED = True

DEBUG = True

DATABASE_CONFIG_ = "Database\config.json"
DATABASE_CONFIG_DB = "Database\icollect_.db"

DATABASE_PATH_ = os.path.join(path_,DATABASE)
DATABASE_PATH_CONFIG = os.path.join(path_,DATABASE_CONFIG_)
DATABASE_PATH_CONFIG_DB = os.path.join(path_, DATABASE_CONFIG_DB)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH_CONFIG_DB




if __name__ == '__main__':
  pass
