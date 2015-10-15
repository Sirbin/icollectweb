__author__ = 'Alessio'

import threading
import Queue
from broker.Mqtt_and_socket import controllo_broker

# import paho.mqtt.client as mqtt
# BROKER ="192.155.90.139"
# PORT = 1883
# TOPIC_Resp = "Collector/Realtime/RXR_Realty/"+"340_Madison_Avenue" +"/#"
# Topic_Pub = "Collector/Setup/RXR_Realty/"+"340_Madison_Avenue"
# topic1 = "Collector/Interval/RXR_Realty/"+"340_Madison_Avenue"+"/#"


class my_data():

    th_name_for_tne = []


queue =Queue.Queue

class connect_to_mqtt(threading.Thread):

    def __init__(self,tne=None,user=None):
        super(connect_to_mqtt,self).__init__(name = "Thread"+tne)


        self.tne = tne
        self.user = str(user)


    def run(self):
        print "start" + self.user,self.tne,self.getName()
        controllo_broker()


if __name__ == '__main__':
     c=connect_to_mqtt("TNEER001067","administrator1")
     my_data.th_name_for_tne.append(c)
     c.start()
     print my_data.th_name_for_tne
