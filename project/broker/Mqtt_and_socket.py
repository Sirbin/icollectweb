__author__ = 'Alessio'
#encoding:utf-8

from project.json_conf_ import create_tenant_building,create_json_table,create_json_building,create_json_tne
from flask_login import current_user
from gevent import monkey
from .view import *
from flask import request,session,current_app
import threading
monkey.patch_all()

# Load json value
json_tne_number = create_json_tne()
json_building = create_json_building()
json_table_meter_value = create_json_table()
json_tenant_building = create_tenant_building()

# configuration Broker

BROKER = "192.155.90.139"
PORT = 1883
TOPIC_Resp = "Collector/Realtime/RXR_Realty/" + str(json_building['collector']['building']) + "/#"
Topic_Pub = "Collector/Setup/RXR_Realty/" + str(json_building['collector']['building'])  # 340_Madison_Avenue"
TOPIC_gen = "Collector/Interval/RXR_Realty/" + str(json_building['collector']['building']) + "/#"  # 340_Madison_Avenue/#"


import json
import time
from flask_socketio import SocketIO, emit, join_room,disconnect,send,leave_room,close_room
import paho.mqtt.client as mqtt

from project import app

socketio = SocketIO(app)





# Broker
def onConnect(client, userdata, rc):
    if rc == 0:
        print "connected"


def controllo_broker(tne,second=None):
        try:
            print("connect......")
            client.loop_start()
            spedisci_dato(tne)
            client.subscribe(TOPIC_Resp, 2)
            client.on_message = onMessage
        except Exception as e:
            '''inserire riconnect to Broker automatico'''
            print "connessione non stanbilita:" + "" + str(e)


def create_json_publish(tne):
    '''
    create a json form to send in broker for pubblish
    '''
    data_create_meter = "realtime" + " " + str(tne)
    return data_create_meter


def onSubscribe(client,userdata,message,tne):
    pass

def onMessage(client, userdata, message):
        print("Topic: " + str(message.topic) + ", Message: " + str(message.payload))
        message_split = message.topic.split('/')
        if message_split[1] == "Realtime":
            stringa_ = json.loads(message.payload)
            socketio.emit('gauge_responce_van', {'valore': stringa_["VaN"]},namespace='/test',room=message_split[4])
            socketio.emit('gauge_responce_vbn', {'valore': stringa_['VbN']},namespace='/test',room=message_split[4])
            socketio.emit('gauge_responce_vcn', {'valore': stringa_['VcN']},namespace='/test',room=message_split[4])
            socketio.emit('gauge_responce_ian', {'valore': stringa_['Ia']},namespace='/test',room=message_split[4])
            socketio.emit('gauge_responce_ibn', {'valore': stringa_['Ib']},namespace='/test',room=message_split[4])
            socketio.emit('gauge_responce_icn', {'valore': stringa_['Ic']},namespace='/test',room=message_split[4])
            socketio.emit('gauge_responce_phase', {'valore': stringa_['PhAI'],'valore1':stringa_['PhBI'],'valore2':stringa_['PhCI']},namespace='/test',room=message_split[4])
            spedisci_dato(message_split[4],session.get('time'))
            '''Problema con session'''
            #client.loop_start()
            #with ctx1:
                #ctx1.push()
                #a= session['tne'] = 'qualkosa'
                #print session.get('time')
                #print ctx1.session
            #client.publish(topic=Topic_Pub, payload=create_json_publish(message_split[4]), qos=2)



# def take_second():
#     ctx = app.test_request_context()
#     ctx1 = app.app_context()
#     print ctx1.g,ctx.session
#     with ctx:
#         print request.args.get('time_gauge')
#         return request.form.get('time_gauge')

def spedisci_dato(tne, second=None):
    second = 2
    while second != 0:
        second -= 1
        time.sleep(2)
        print second
        if second == 0:
            return client.publish(topic=Topic_Pub, payload=create_json_publish(tne), qos=2)

@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response', {"data": message['data']})


@socketio.on('connect', namespace="/test")
def test_connect():
    emit('status',{'data': 'Connect!!'})

@socketio.on('disconnect', namespace="/test")
def test_disconnect():
    left()
    session.pop('tne')
    print ('Client disconnect')

@socketio.on('join', namespace='/test')
def join(message):
        room = session.get('tne')
        join_room(room)
        emit('status',{'data': current_user.user+":"+' create a socket_io'+ room},room=room)

@socketio.on('left',namespace='/test')
def left(message=None):
    room = session.get('tne')
    print 'my room',room
    leave_room(room)
    print "eliminato"
    emit('status',{'data':current_user.user+":"+'leave a socket_io'+room },room=room)

@socketio.on('message')
def handle_message(message):
    print ('recive message' + message)

try:
    client = mqtt.Client(client_id="", clean_session=True, userdata=None, protocol="MQTTv31")
    client.connect(BROKER, port=1883, keepalive=60, bind_address="")
    client.on_connect = onConnect
except Exception as e:
    '''inserire reconnect to broker'''
    print "Error on mqtt"+ e


if __name__ == '__main__':
    pass
