'''Json Parse

author : alessio
date : 05/01/2015

'''

import json,os,sqlite3,time
from config_ import DATABASE_PATH_CONFIG

all_data_meters = []

# '''Path'''
# conn_database = "C:\\Users\\Alessio\\Dropbox\\Progetto_Collect_with_Flask\\icollect\\database"
#
# databaseMeters = os.path.join(conn_database, "meters_log.db")

def create_json_tne():
    try:
        with open(DATABASE_PATH_CONFIG, "r") as JsonConn:
            meters_data = json.load(JsonConn)
            if 'collector' in meters_data:
                meters_value = []
                meters_value_tnenumber = []
                for meter_all in meters_data["gateways"]["meters"]:
                     meters_value.append(meter_all)
                for meter_all_tne in meters_value:
                     meters_value_tnenumber.append(meter_all_tne["tne_number"])
                return meters_value_tnenumber

            else:
                print ("Collector not present, json not present")
    except:
        JsonConn.close()
        return False

def create_json_table():
    try:
        with open(DATABASE_PATH_CONFIG, "r") as JsonConn:
            meters_data = json.load(JsonConn)
            meter_value = []
            for meter_all in meters_data["gateways"]["meters"]:
                meter_value.append(meter_all)
            return meter_value
    except:
        JsonConn.close()
        return False




def create_json_building():
    try:
        with open(DATABASE_PATH_CONFIG, "r") as JsonConn:
            meters_data = json.load(JsonConn)
            return meters_data

    except:
        JsonConn.close()
        return False

def create_tenant_building():
    with open(DATABASE_PATH_CONFIG,"r") as Json:
        meter_data = json.load((Json))
        meters_temp = []
        tenant_temp = []
        for k in meter_data['gateways']['meters']:
            meters_temp.append(k)
        for j in meters_temp:
            tenant_temp.append(j['tenant_name'])
        create_dict_tenant= dict((c,tenant_temp.count(c)) for c in tenant_temp)
        return create_dict_tenant
        create_tenant_number  = list((m) for m in list(create_dict_tenant.keys()))
        return create_tenant_number
        #print len(create_tenant_number)


def estraikey(jsonstring,key):
        if jsonstring == None:
            return False
        if key in jsonstring:
            return jsonstring[key]
        return False

# Create Database for Log


# for k,v in tne.items():
#                     if tne[k] != None:
#                         if k == None:
#                             print "none",tne[k]
#                             break
#                     print "normal",k,tne[k]

# def databasemeters(tnenumber,date):
#     conn = sqlite3.connect(databaseMeters)
#     cur = conn.execute('SELECT * FROM meter_data WHERE tnenumber=? AND date=?', [tnenumber, date])
#     for row in cur.fetchone():
#         meter_data = row
#     meter = json.loads(meter_data)
#     return meter
#     conn.close()
#         #print meter_data
#             #meter = json.loads(meter_data)
#             #meter_datasi = request.args.get("prova", int(meter["WhRec"]) / 100)
#             #print int(meter["WhRec"])
#             #return int(meter["WhRec"])
#     #conn.close()
#
# def databasemeters_history_tables(tnenumber,date_start,date_fin):
#     #with sqlite3.connect(databaseMeters) as conn:
#     conn = sqlite3.connect(databaseMeters)
#         #cur = conn.cursor()
#     cur = conn.execute('SELECT * FROM meter_data WHERE tnenumber=? and date>=? and date<=?' ,[tnenumber,date_start,date_fin])
#     #for row in cur.execute('SELECT * FROM meter_data WHERE tnenumber=? and date>=? and date<=?' ,[tnenumber,date_start,date_fin])
#         #print row
#     for row in cur.fetchall():
#             #print row[0] , row[1] , row[3]
#             print json.loads(row[3])
#         # meter_data_history = row
#         # meter_h = []
#         # meter_h.append(meter_data_history)
#         # for date in meter_h:
#         #     print date[0],date[1]
#         #     dr = date[3]
#         #     print json.loads(dr)
#     conn.close()

if __name__ == '__main__':
  create_tenant_building()
