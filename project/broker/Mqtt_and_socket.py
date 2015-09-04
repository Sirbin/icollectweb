__author__ = 'Alessio'

from project.json_conf_ import create_tenant_building,create_json_table,create_json_building,create_json_tne

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
#from project import socketio
from flask_socketio import SocketIO, emit
from gevent import monkey
import paho.mqtt.client as mqtt
from project import app

monkey.patch_all()

socketio = SocketIO(app)

 # Broker
def onConnect(client, userdata, rc):
    if rc == 0:
        print "connected"


def controllo_broker(tne=None):
    try:
        status = client.loop_start()
        print "lo status", status
        print("connect......")
        client.connect(BROKER, port=1883, keepalive=60, bind_address="")
        client.on_connect = onConnect
        spedisci_dato(tne)
        client.subscribe(TOPIC_Resp, 2)
        client.on_message = onMessage
        # client.unsubscribe(TOPIC_Resp)
    except Exception as e:
        print "connessione non stanbilita:" + "" + str(e)


def create_json_publish(tne):
    '''
    create a json form tO send in broker for pubblish
    '''
    data_create_meter = "realtime" + " " + str(tne)
    return data_create_meter


def onMessage(client, userdata, message):
    print("Topic: " + str(message.topic) + ", Message: " + str(message.payload))
    message_split = message.topic.split('/')
    if message_split[1] == "Realtime":
        stringa_ = json.loads(message.payload)
        print stringa_['VaN'], stringa_['VbN']
        socketio.emit('gauge_responce', {'valore': stringa_["VaN"]}, namespace='/test')
        socketio.emit('gauge_responce_vbn', {'valore': stringa_['VbN']}, namespace='/test')
        spedisci_dato(message_split[4])
    else:
        print ("stop")


def spedisci_dato(tne, second=None):
    conteggio = 2
    while conteggio != 0:
        conteggio -= 1
        time.sleep(2)
        print conteggio
        if conteggio == 0:
            return client.publish(topic=Topic_Pub, payload=create_json_publish(tne), qos=2)


@socketio.on('my event', namespace="/test")
def test_message(message):
    emit('my response', {"data": message['data']})


@socketio.on('connect', namespace="/test")
def test_connect():
    emit('my responce', {"data": "Connect"})

client = mqtt.Client(client_id="", clean_session=True, userdata=None, protocol="MQTTv31")



if __name__ == '__main__':
    pass

