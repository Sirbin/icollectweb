'''Icollect Programm With Flask Framework

author : alessio
date : 05/04/2015
'''


# !/usr/bin/python
# -*- coding: ascii -*-
import json
from datetime import datetime
import logging
import threading

from flask import Flask, render_template, redirect, url_for, session, flash, request
from gevent import monkey
from flask_socketio import SocketIO, emit
import paho.mqtt.client as mqtt
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment

from project.json_conf_ import create_json_building, create_json_table, create_json_tne, create_tenant_building
from Py_Error.database_icollet import *

__vers__ = 1
__status__ = 'Unstable'
# __status__='Stable'
__version_date__ = '08/21/2015'

# # Load json value
# json_tne_number = create_json_tne()
# json_building = create_json_building()
# json_table_meter_value = create_json_table()
# json_tenant_building = create_tenant_building()

logging.basicConfig(level=logging.DEBUG)
monkey.patch_all()

# application Flask
app = Flask(__name__)

# application moment for time e location
moment = Moment(app)

# applications Socketio
socketio = SocketIO(app)

# connect to config_.py
app.config.from_object('config_')

# SqlAlchemy
db = SQLAlchemy(app)

# import after db
from model_ import gauge_

# # configuration Broker
# BROKER = "192.155.90.139"
# PORT = 1883
# TOPIC_Resp = "Collector/Realtime/RXR_Realty/" + str(json_building['collector']['building']) + "/#"
# Topic_Pub = "Collector/Setup/RXR_Realty/" + str(json_building['collector']['building'])  # 340_Madison_Avenue"
# topic1 = "Collector/Interval/RXR_Realty/" + str(json_building['collector']['building']) + "/#"  # 340_Madison_Avenue/#"
# mythr = []



# # funzioni errori pagina
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html', current_time=datetime.utcnow()), 404
#
#
# @app.errorhandler(500)
# def server_internal_error(e):
#     return render_template('500.html', current_time=datetime.utcnow()), 500


# Funcion to login
# def login_required(test):
#     @wraps(test)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return test(*args, **kwargs)
#         else:
#             flash('You need to login first.')
#             return redirect(url_for('login_'))
#     return wrap


# # funzione errori campi
# def flask_error(form):
#     for field, errors in form.error.itemes():
#         for error in errors:
#             flash('Error in the %s field - %s' % (getattr(form, field).label.text, error), 'error')


 # # Funzione Users Login
# @users_for_blueprint.route('/', methods=['GET', 'POST'])
# def login_():
#     error = None
#     form = login_users(request.form)
#     if request.method == 'POST':
#         if form.validate_on_submit():
#             user = user_.query.filter_by(user=form.user_login.data).first()
#             if user is not None and bycrypt_on_pass_user.check_password_hash(user.password,request.form['user_password']):
#                 #login_user(user,form.user_remember.data)
#                 session['logged_in'] = True
#                 session['user_id'] = user.id_user
#                 session['user'] = user.user
#                 session['profile'] = user.role
#                 flash("you are logged Welcome %s" % session['user'])
#                 now_time =datetime.now()
#                 user_logging = Logging(user_connect_=None)
#                 user_logging.create_login_info(session['user'],now_time.strftime('%d-%m-%Y %H-%M-%S'), request.url)
#                 #return redirect(request.args.get('next') or url_for('general.dashboard_'))
#                 return render_template('dashboard_.html', username=session['user'], current_time=datetime.utcnow())
#             else:
#                 error = "Invalid User or Password"
#         else:
#             error = "Both Field are required"
#     return render_template("Login.html", form=form, error=error)
#


# # Funzione Logout
# @app.route('/logout')
# @login_required
# def logout_():
#     session.pop('logged_in', None)
#     session.pop('user_id', None)
#     session.pop('user',None)
#     session.pop('profile',None)
#     flash('Goodbye')
#     return redirect(url_for('login_'))


# Pagina Principale dashbord da creare
# @app.route('/dashboard')
# @login_required
# def dashboard_():
#     return render_template('dashboard_.html', username=session['user'], current_time=datetime.utcnow())


# @app.route('/dashboard/building')
# @login_required
# def building_():
#     if json_building != False:
#         return render_template('building.html', json_building=json_building, json_tne_number=json_tne_number,
#                                json_table_meter_value=json_table_meter_value,
#                                json_tenant_building=json_tenant_building, username=session['user'],
#                                current_time=datetime.utcnow())
#     return redirect(url_for('dashboard_'))


# @app.route('/dashboard/tenant')
# @login_required
# def tenant_():
#     return render_template("tenant.html", json_tenant_building=json_tenant_building,
#                            json_building=json_building, username=session['user'], current_time=datetime.utcnow())


# @app.route("/dashboard/tenant/<tenant>")
# @login_required
# def tenant_name_(tenant):
#     if json_building != False:
#         return render_template('tenant_name.html', tenant=tenant, username=session['user'],
#                                current_time=datetime.utcnow())
#     return redirect(url_for('tenant.html'))

# @app.route("/dashboard/meters")
# @login_required
# def meters_():
#     if json_building != False:
#         return render_template('meters.html', json_tenant_building=json_tenant_building,
#                                json_table_meter_value=json_table_meter_value,
#                                json_building=json_building, username=session['user'], current_time=datetime.utcnow())


# @app.route("/dashboard/meters/<meters>", methods=["GET"])
# @login_required
# def tables_history_meters(meters):
#     if json_building != False:
#         for tne in json_table_meter_value:
#             if meters == tne['tne_number'] and request.method == "GET":
#                 print "la base", request.base_url
#                 print "prova", request.args.get(session['user'])
#                 myth = threading.Thread(target=controllo_broker, args=(meters,))
#                 myth.run()
#                 # associate_tne_th = dict({meters:myth})
#                 # mythr.append(associate_tne_th)
#                 # mythr[meters].start()
#                 return render_template('meters_name.html', tne=meters, username=session['user'],
#                                        current_time=datetime.utcnow())
#     flash("Json not found")
#     return redirect(url_for('dashboard_'))


# @app.route("/dashboard/setting", methods=['GET', 'POST'])
# @login_required
# def setting_():
#     user_gauge_id = session['user_id']
#     gauge_user_user_id = gauge_.query.filter_by(id_=user_gauge_id).first()
#     form = form_check_gauge(request.form)
#     if request.method == "POST":
#             if user_gauge_id == gauge_user_user_id.id_:
#                 print form.name_checked_gauge_van.data
#                 print form.name_change_gauge_van.data
#                 db.session.query(gauge_).update(
#                     { "name_gauge_change":form.name_change_gauge_van.data,"gauge_choiche":str(form.name_checked_gauge_van.data)})
#                 db.session.commit()
#                 flash("aggiornato")
#                 return redirect(url_for("setting_"))
#     #     if gauge_user_user_id is None:
#     #         redirect(url_for('dashboard_'))
#     #     else:
#     #         gauge_select = gauge_(form.name_change_gauge_van.label.text, form.name_change_gauge_van.data,
#     #                           str(form.name_checked_gauge_van.data), session['user_id'])
#     #         try:
#     #             db.session.merge(gauge_select)
#     #             db.session.commit()
#     #             flash("Gauge saved")
#     #             dato_van_check = str(form.name_checked_gauge_van.data)
#     #             print "check_van", dato_van_check
#     #             id_van = form.name_checked_gauge_van.id
#     #             print "id _ck", id_van
#     #             print "txt", form.name_change_gauge_van.data
#     #             return redirect(url_for('setting_'))
#     #         except IntegrityError:
#     #             flash ("errore")
#     #             return redirect(url_for('setting_'))
#     #     #return render_template('setting_.html', form=form, username=session['user'], current_time=datetime.utcnow())
#     return render_template('setting_.html', form=form, username=session['user'], current_time=datetime.utcnow(),name_controll = gauge_user_user_id)


# # da cancellare solo prova gauge
# @app.route('/dashboard/prova')
# def gauge_prova():
#         user_gauge_id = session['user_id']
#         gauge_user_user_id = db.session.query(gauge_).filter_by(id_=user_gauge_id)
#         if gauge_user_user_id is not None:
#             for t in gauge_user_user_id:
#                 print t.id_, t.name_gauge_change, t.gauge_choiche
#                 value_tot = {"id":t.id_ ,"name":t.name_gauge_change,"choice":t.gauge_choiche}
#             return render_template('prova.html',username=session['user'], current_time=datetime.utcnow(),scelta_van =str(t.gauge_choiche) )
#         return redirect(url_for('dashboard_'))





# @app.route('/dashboard/users')
# @login_required
# def user_page():
#     users = db.session.query(user_).order_by(user_.id_user)
#     return render_template('users.html', users=users, username=session['user'], current_time=datetime.utcnow())


# @app.route('/dashboard/users/new_user', methods=['GET', 'POST'])
# @login_required
# def new_users():
#     error = None
#     form = register_user(request.form)
#     if request.method == "POST":
#         if form.validate_on_submit():
#             new_user = user_(form.user.data, form.password.data, form.email.data, form.first_name.data,
#                              form.last_name.data, str(form.select_profile.data))
#             try:
#                 db.session.add(new_user)
#                 db.session.commit()
#                 flash('New user register')
#                 return redirect(url_for('user_page'))
#             except IntegrityError:
#                 error = "username and/or email exist"
#                 return render_template('new_users.html', form=form, error=error, username=session['user'],
#                                        current_time=datetime.utcnow())
#     return render_template('new_users.html', form=form, error=error, username=session['user'],
#                            current_time=datetime.utcnow())


# @app.route('/dashboard/users/edit/<useredit>', methods=['POST', 'GET'])
# @login_required
# def edit_users(useredit):
#     error = None
#     form = register_user(request.form)
#     useredit_change = useredit
#     query_for_change_user = user_.query.filter_by(user=useredit_change)
#     if request.method == "POST":
#         if form.validate_on_submit():
#             try:
#                 db.session.query(user_).filter_by(user=useredit_change).update(
#                     {"user": form.user.data, "profile_type": form.select_profile.data, "password": form.password.data,
#                      "email": form.email.data, "first_name": form.first_name.data, "last_name": form.last_name.data})
#                 db.session.commit()
#                 flash('User %s' % form.user.data, 'Update')
#                 return redirect(url_for('user_page'))
#             except IntegrityError:
#                 error = "username and/or email are exist"
#                 return render_template('edit_user.html', useredit_change=query_for_change_user, form=form, error=error,
#                                        usernam=session['user'], current_time=datetime.utcnow())
#     return render_template('edit_users.html', user_change=query_for_change_user, form=form, username=session['user'],
#                            error=error, current_time=datetime.utcnow())


# @app.route('/dashboard/users/<usersdel>')
# @login_required
# def delete_users(usersdel):
#     error = None
#     if session['profile'] == "admin":
#         delete_us = usersdel
#         db.session.query(user_).filter_by(user=delete_us).delete()
#         db.session.commit()
#         flash('users delete')
#         return redirect(url_for('user_page'))
#     else:
#         error = 'User {0} is not Administrator'.format(session['user'])
#         flash('User {0} is not Administrator'.format(session['user']))
#         return redirect(url_for('user_page'),error=error)



# Broker
# def onConnect(client, userdata, rc):
#     if rc == 0:
#         print "connected"
#
#
# def controllo_broker(tne):
#     try:
#         status = client.loop_start()
#         print "lo status", status
#         print("connect......")
#         client.connect(BROKER, port=1883, keepalive=60, bind_address="")
#         client.on_connect = onConnect
#         spedisci_dato(tne)
#         client.subscribe(TOPIC_Resp, 2)
#         client.on_message = onMessage
#         # client.unsubscribe(TOPIC_Resp)
#     except Exception as e:
#         print "connessione non stanbilita:" + "" + str(e)
#
#
# def create_json_publish(tne):
#     '''
#     create a json form tO send in broker for pubblish
#     '''
#     data_create_meter = "realtime" + " " + str(tne)
#     return data_create_meter
#
#
# def onMessage(client, userdata, message):
#     print("Topic: " + str(message.topic) + ", Message: " + str(message.payload))
#     message_split = message.topic.split('/')
#     if message_split[1] == "Realtime":
#         stringa_ = json.loads(message.payload)
#         print stringa_['VaN'], stringa_['VbN']
#         socketio.emit('gauge_responce', {'valore': stringa_["VaN"]}, namespace='/test')
#         socketio.emit('gauge_responce_vbn', {'valore': stringa_['VbN']}, namespace='/test')
#         spedisci_dato(message_split[4])
#     else:
#         print ("stop")
#
#
# def spedisci_dato(tne, second=None):
#     conteggio = 2
#     while conteggio != 0:
#         conteggio -= 1
#         time.sleep(2)
#         print conteggio
#         if conteggio == 0:
#             return client.publish(topic=Topic_Pub, payload=create_json_publish(tne), qos=2)
#
#
# @socketio.on('my event', namespace="/test")
# def test_message(message):
#     emit('my response', {"data": message['data']})
#
#
# @socketio.on('connect', namespace="/test")
# def test_connect():
#     emit('my responce', {"data": "Connect"})

# @app.route("/dashbord/<name>", methods=['GET'])
# def tne(name):
#     #json_table_meter_value = jsontable()
#     #time.strftime("%Y-%m-%d").replace("2015-04-23"))
#     database_meters_VaN = estraikey(databasemeters((name[7:]),str("2015-04-23")), "VaN")
#     database_meters_VbN = estraikey(databasemeters((name[7:]),str("2015-04-23")),"VbN")
#     database_meters_VcN = estraikey(databasemeters((name[7:]),str("2015-04-23")),"VcN")
#     database_meters_Ia = estraikey(databasemeters((name[7:]),str("2015-04-23")),"Ia")
#     database_meters_Ib = estraikey(databasemeters((name[7:]), str("2015-04-23")),"Ib")
#     database_meters_Ic = estraikey(databasemeters((name[7:]), str("2015-04-23")),"Ic")
#     database_meters_PhAI = estraikey(databasemeters((name[7:]),str("2015-04-23" )),"PhAI")
#     database_meters_PhBI = estraikey(databasemeters((name[7:]),str("2015-04-23")),"PhBI")
#     database_meters_PhCI = estraikey(databasemeters((name[7:]),str("2015-04-23")),"PhCI")
#     database_meters_ctnum = estraikey(databasemeters((name[7:]),str("2015-04-23")),"ctnum")
#     with open(jsonPath, "r") as JsonConn:
#             Meters_Data = json.load(JsonConn)
#             json_building1 = Meters_Data["collector"]["building"]
#             for Meter_all in Meters_Data["gateways"]["meters"]:
#                     while name == Meter_all['tne_number']:
#                         return render_template("meters_.html", tnen=estraikey(Meter_all,'tne_number'), serial = estraikey(Meter_all,'serial_number'), model = estraikey(Meter_all,'meter_model'), name = estraikey(Meter_all,'tenant_name'),
#                             protocol = estraikey(Meter_all,'protocol'),brand = estraikey(Meter_all,'meter_brand'), slave = estraikey(Meter_all,'slave_number'), wireless = estraikey(Meter_all,'wireless'),
#                             address = estraikey(Meter_all,'address'), json_tnenumber = json_tnenumber , json_building = json_building1,
#                            database_meters_VaN = database_meters_VaN, database_meters_VbN=database_meters_VbN,
#                            database_meters_VcN = database_meters_VcN,database_meters_Ia=database_meters_Ia,
#                            database_meters_Ib=database_meters_Ib,database_meters_Ic=database_meters_Ic,
#                            database_meters_PhAI = database_meters_PhAI,database_meters_PhBI = database_meters_PhBI,
#                            database_meters_PhCI = database_meters_PhCI, database_meters_ctnum = database_meters_ctnum)
#             return render_template('meters_.html', json_tnenumber=json_tnenumber, json_building=json_building )#, json_table=json_table)

# def JsonTne():
# with open(jsonPath, "r") as JsonConn:
# Meters_Data = json.load(JsonConn)
#        Meters_Value = []
#        Meters_Value_TneNumeber =[]
#        for Meter_all in  Meters_Data["gateways"]["meters"]:
#             Meters_Value.append(Meter_all)
#        for Meter_Num in Meters_Value:
#             Meters_Value_TneNumeber.append(Meter_Num["tne_number"])
#     return Meters_Value_TneNumeber


#
#
# @app.route("/")
# def database():
#     try:
#         #g.db = sqlite3.connect(databases)connectDb()
#         conn = sqlite3.connect(app.database1)
#         #cur = g.db.execute('SELECT * FROM meter_data WHERE tnenumber=? and time=?', [1188, '09:40:00'])
#         cur = conn.execute('SELECT * FROM meter_data WHERE tnenumber=? and time=?', [1188, '09:40:00'])
#         for row in cur.fetchone():
#             meter_data = row
#         #g.db.close()
#         conn.close()
#         print meter_data
#         meter = json.loads(meter_data)
#         meter_datasi = request.args.get("prova", int(meter["WhRec"]) / 100)
#
#
#         #meter_data = [dict(json=row[3])] #for row in cur.fetchall()
#         #met=json.loads(meter_data)
#
#         return render_template('index.html', prova=meter_datasi)
#     except Exception as e:
#         return (str("Impossibile connettersi " + e))
#

#
# def querytne():
#         conn = sqlite3.connect(databases)
#         #cur = g.db.execute('SELECT * FROM meter_data WHERE tnenumber=? and time=?', [1188, '09:40:00'])
#         cur = conn.execute('SELECT tnenumber FROM meter_data WHERE time=?',["05:49:00"])
#         for row in cur.fetchall():
#             meter_data1 = row
#             print meter_data1
#         #g.db.close()
#         conn.close()
#         # meter = json.loads(meter_data)
#         # meter_datasi = request.args.get("prova", int(meter["WhRec"]) / 100)
#         # return render_template(bas.html', prova=meter_datasi)

# @app.route("/tables/")
# def tables():
#     nome = request.args.get('nome', 'alessio')
#     return render_template('index.html', nome=nome)
#
# @app.add_template_filter
# def JsonTne():
#     with open(jsonPath, "r") as JsonConn:
#        Meters_Data = json.load(JsonConn)
#        Meters_Value = []
#        Meters_Value_TneNumeber =[]
#        for Meter_all in  Meters_Data["gateways"]["meters"]:
#             Meters_Value.append(Meter_all)
#        for Meter_Num in Meters_Value:
#             Meters_Value_TneNumeber.append(Meter_Num["tne_number"])
#     return Meters_Value_TneNumeber
# def processo():
#     while True:
#         num = randint(0,100)
#     print num
#     return num
# client = mqtt.Client(client_id="", clean_session=True, userdata=None, protocol="MQTTv31")
if __name__ == '__main__':
    pass
