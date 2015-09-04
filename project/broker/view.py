__author__ = 'Alessio'

from datetime import datetime
from functools import wraps
from flask import render_template, redirect, url_for, session, flash, Blueprint,request
from project.json_conf_ import create_tenant_building,create_json_table,create_json_building,create_json_tne
from Mqtt_and_socket import controllo_broker
import threading

#configuration Json
json_tne_number = create_json_tne()
json_building = create_json_building()
json_table_meter_value = create_json_table()
json_tenant_building = create_tenant_building()


#config
blueprint_mqtt_data = Blueprint('Mqtt',__name__)

# Function help
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login_'))
    return wrap

@blueprint_mqtt_data.route("/dashboard/meters/<meters>", methods=["GET"])
@login_required
def tables_history_meters(meters):
    if json_building != False:
        for tne in json_table_meter_value:
            if meters == tne['tne_number'] and request.method == "GET":
                print "la base", request.base_url
                print "prova", request.args.get(session['user'])
                myth = threading.Thread(target=controllo_broker, args=(meters,))
                myth.run()
                # associate_tne_th = dict({meters:myth})
                # mythr.append(associate_tne_th)
                # mythr[meters].start()
                return render_template('meters_name.html', tne=meters, username=session['user'],
                                       current_time=datetime.utcnow())
    flash("Json not found")
    return redirect(url_for('dashboard_'))