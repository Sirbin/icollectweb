__author__ = 'Alessio'

from datetime import datetime
from functools import wraps
from project import db
from  project.model_ import gauge_
from flask import render_template, redirect, url_for, session, flash, Blueprint,copy_current_request_context
from project.json_conf_ import create_tenant_building,create_json_table,create_json_building,create_json_tne
from Mqtt_and_socket import controllo_broker
import threading
from flask_login import login_required,current_user


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
        user_gauge_model_id = current_user.id_user
        gauge_query_id_user = db.session.query(gauge_).filter_by(id_=user_gauge_model_id)
        if gauge_query_id_user is not None:
            for t in gauge_query_id_user:
                 print t.id_, t.name_gauge_change, t.gauge_choiche
            for tne in json_table_meter_value:
                if meters == tne['tne_number']:
                    session['tne'] = meters
                    myth = threading.Thread(target=controllo_broker,args=(meters,))
                    myth.start()
                    return render_template('meters_name.html',tne=meters,json_building=json_building,
                                       tenant = json_tenant_building,json_table_meter_value=json_table_meter_value,current_time=datetime.utcnow(),
                                           value_boolen_gauge_id = t.gauge_choiche,value_name_gauge_id=t.name_gauge_change)
    flash("Json not found")
    return redirect(url_for('dashboard_'))

