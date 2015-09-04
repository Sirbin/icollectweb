__author__ = 'Alessio'

from datetime import datetime
from flask import render_template, Blueprint


blueprints_error = Blueprint('error',__name__)

#funzioni errori pagina
@blueprints_error.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', current_time=datetime.utcnow()), 404


@blueprints_error.errorhandler(500)
def server_internal_error(e):
    return render_template('500.html', current_time=datetime.utcnow()), 500
