__author__ = 'Alessio'

from project import db
from project.config_ import DATABASE_PATH_CONFIG_DB
import sqlite3
#try:
with sqlite3.connect(DATABASE_PATH_CONFIG_DB) as con:
          c = con.cursor()
#         c.execute('''ALTER TABLE gauge_select RENAME TO gauge_select_old''')
#         c.execute('''CREATE TABLE IF NOT EXISTS user_data (id_ INTEGER PRIMARY KEY  ,username text NOT NULL , password text NOT NULL , email text NOT NULL ,data  DATE )''')
#         c.execute('''CREATE TABLE IF NOT EXISTS gauge_select_prova (id_gauge INTEGER PRIMARY KEY AUTOINCREMENT ,name_gauge text, gauge_choiche text , id_ integer)''')
#         print "tabella creata con successo"
#         try:
#             # c.execute('''SELECT * FROM user_data''')
#             # my = (dict(name=row[0]) for row in c.fetchall())
#             # print my
          c.execute('''INSERT INTO user_data VALUES (?,?,?,?,?)''',('1','admin','admin','admin@admin',time.strftime("%Y-%m-%d")))
#             #c.execute('''INSERT INTO user_data VALUES (?,?,?,?,?)''',('2','ciccio','ciccio','asmin@admin',time.strftime("%Y-%m-%d")))
#             #c.execute('''INSERT INTO user_data VALUES (?,?,?,?,?)''',(None,'ciccio1','ciccio1','asmin@admin',time.strftime("%Y-%m-%d")))
#             c.execute('''INSERT INTO gauge_select_prova VALUES (?,?,?,?)''',(None,"we","soca",1))
#except Exception as e:
#             print "Impossibile inserire il dato",e
# except Exception as e:
#     print "Impossibile connettersi",e


db.create_all()


#db.session.add(user_("admin","admin","admin@admin.it","alessio","bino","admin"))

#db.session.commit()








