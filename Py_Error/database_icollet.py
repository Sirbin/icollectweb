__author__ = 'Alessio'

import os,time
import sqlite3
from project.config_ import DATABASE_PATH_CONFIG_DB



class icol_db(object):

    def __init__(self):
        #super(icol_db,self).__init__()
        try:
            self.con = sqlite3.connect(DATABASE_PATH_CONFIG_DB)
            print "Connect with database as success"
        except Exception:
            print "Error connect to database"

    def sel_all_db(self,username):
         c = self.con.execute('''SELECT * FROM user_data WHERE username=?''', [str(username)])
         self.use_dict_for_login = sorted([dict(id=row[0],username=row[1],password=row[2],email=row[3],data=row[4]) for row in c.fetchall()])
         print self.use_dict_for_login
         return self.use_dict_for_login

    def insert_gauge_select(self,id_gauge,name_gauge,gauge_choice,id_user):
            self.id_gauge = id_gauge
            self.name_gauge=name_gauge
            self.gauge_choice=gauge_choice
            self.id_user = id_user
            try:
                self.con.execute('''INSERT INTO gauge_select_prova VALUES (?,?,?,?)''',(id_gauge,name_gauge,gauge_choice,id_user))
                self.con.commit()
                print "Insert with success"
            except Exception as e:
                print "Error database insert",e

if __name__ == '__main__':
    pass


