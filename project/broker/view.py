__author__ = 'Alessio'

from datetime import datetime
from functools import wraps
from project import db
from  project.model_ import gauge_
from flask import render_template, redirect, url_for, session, flash, Blueprint,copy_current_request_context,request
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


@blueprint_mqtt_data.route("/dashboard/meters/<meters>", methods=["GET","POST"])
@login_required
def tables_historynot_meters(meters):
    name_change_gauge_dict = {}
    user_gauge_model_id = current_user.id_user
    gauge_query_id_user = db.session.query(gauge_).filter_by(id_=user_gauge_model_id)
    for t in gauge_query_id_user:
        name_change_gauge_dict[t.name_gauge] =  dict(name_gauge_choiche = t.gauge_choiche, name_gauge_change = t.name_gauge_change)
    print len(name_change_gauge_dict)
    print name_change_gauge_dict
    for tne in json_table_meter_value:
        if meters == tne['tne_number']:
            if len(name_change_gauge_dict) !=0:
                session['tne'] = meters
                if request.method == 'POST':
                   d = session['time'] = int(request.form.get('time_gauge'))
                myth = threading.Thread(target=controllo_broker,args=(tne,))
                myth.start()
                return render_template('meters_name.html',tne=meters,json_building=json_building,
                                        tenant = json_tenant_building,json_table_meter_value=json_table_meter_value,current_time=datetime.utcnow(),
                                        name_change_gauge_dict=name_change_gauge_dict)
            flash("Insert your setting")
            return render_template('meters_name.html',tne=meters,json_building=json_building,
                                        tenant = json_tenant_building,json_table_meter_value=json_table_meter_value,current_time=datetime.utcnow(),
                                        name_change_gauge_dict=name_change_gauge_dict)

