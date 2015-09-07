__author__ = 'Alessio'

import sqlite3
from project.config_ import DATABASE_CONFIG_DB
from project import db
from project.model_ import user_
from project import bycrypt_on_pass_user

#try:
 #   with sqlite3.connect(DATABASE_CONFIG_DB) as con:
  #      c = con.cursor()
        #c.execute('''DROP TABLE gauge_select''')
        #c.execute('''ALTER TABLE gauge_select RENAME TO gauge_select_old''')
        #c.execute('''INSERT INTO gauge_select_prova VALUES (?,?,?,?)''',(None,"we","soca",1))
#except Exception as e:
 #       print "Impossibile inserire il dato",e

# crea la nuova tabella
#db.create_all()

# aggiunge alla tabella user il dato
db.session.add(user_("admin11",bycrypt_on_pass_user.generate_password_hash('allpowerful'),"admin11211@admin.it","alessio1","bino1","admin"))

db.session.commit()








