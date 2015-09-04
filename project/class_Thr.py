__author__ = 'Alessio'

import threading
import Queue
import paho.mqtt.client as wer
BROKER ="192.155.90.139"
PORT = 1883
TOPIC_Resp = "Collector/Realtime/RXR_Realty/"+"340_Madison_Avenue" +"/#"
Topic_Pub = "Collector/Setup/RXR_Realty/"+"340_Madison_Avenue"
topic1 = "Collector/Interval/RXR_Realty/"+"340_Madison_Avenue"+"/#"



queue =Queue.Queue

class mqtt():


    def __init__(self):

        self.th = threading.Thread(target=self.run)

        self.queue = queue


    def cont(self):

        self.clienta = wer.Client(client_id="", clean_session=True, userdata=None, protocol="MQTTv31")
        self.clienta.loop_start()
        self.clienta.connect(BROKER,port=1883,keepalive=60,bind_address="")
        self.clienta.on_connect = self.onConnect
        self.clienta.on_subscribe(Topic_Pub,2)
        self.clienta.on_message = self.onMessage


    def run(self):
        print "connecto t"


    def onConnect(self,rc,mosq,obj):
        if rc == 0:
            print "Connect successfully"

    def onMessage(self,message,mosq,obj):
            print "messaggio topic"+message.topic+"messagio pauload"+str(message.payload)

    def onDisconnect(self):
        pass


if __name__ == '__main__':
    pass