__author__ = 'Alessio'

from datetime import datetime
from functools import wraps
from project import app
from flask import render_template, redirect, url_for, session, flash, Blueprint,copy_current_request_context
from project.json_conf_ import create_tenant_building,create_json_table,create_json_building,create_json_tne
from Mqtt_and_socket import controllo_broker,create_json_publish
import threading
from flask_login import login_required,current_user
from flask_socketio import SocketIO,join_room,emit

#configuration Json
json_tne_number = create_json_tne()
json_building = create_json_building()
json_table_meter_value = create_json_table()
json_tenant_building = create_tenant_building()


#config
blueprint_mqtt_data = Blueprint('Mqtt',__name__)


@blueprint_mqtt_data.route("/dashboard/meters/<meters>", methods=["GET"])
@login_required
def tables_history_meters(meters):
    if json_building != False:
        for tne in json_table_meter_value:
            if meters == tne['tne_number']:
                session['tne'] = meters
                print session['tne']
                #print "la base", request.url[43 :]
                myth = threading.Thread(target=controllo_broker,args=(meters,))
                #print "nome" ,myth.getName()
                myth.start()
                # prova1 = dict({meters:myth})
                # my_data.prova.append(prova1)
                # print "lista",my_data.prova
                # print "lista2",my_data.prova[0]
                #
                # for c in my_data.prova:
                #     for key, value in c.items():
                #
                #             #value.join()



                return render_template('meters_name.html',tne=meters,json_building=json_building,
                                       tenant = json_tenant_building,
                                       current_time=datetime.utcnow())
    flash("Json not found")
    return redirect(url_for('dashboard_'))

