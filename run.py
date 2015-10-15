__author__ = 'Alessio'

import os
from socket import gethostname,gethostbyname
from project import app,socketio
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
host=gethostbyname(gethostname())

if __name__ == '__main__':
        # er = socketio.run(app,host=host)
        # http_server = HTTPServer(WSGIContainer(wsgi_application=er))
        # http_server.listen(5000)
        # IOLoop.instance().start()
        socketio.run(app,host=host)

