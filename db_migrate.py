__author__ = 'Alessio'

import sqlite3
from project.config_ import DATABASE_PATH_CONFIG_DB
from project import db
from project.model_ import user_, gauge_,profile_type_
from project import bycrypt_on_pass_user

#try:
#with sqlite3.connect(DATABASE_PATH_CONFIG_DB) as con:
        #c = con.cursor()
        #c.execute('''DROP TABLE gauge_select''')
        #c.execute('''DROP TABLE user''')
        #c.execute('''DROP TABLE profile_type''')

        #c.execute('''ALTER TABLE user RENAME TO user_old''')
        #c.execute('''INSERT INTO gauge_select_prova VALUES (?,?,?,?)''',(None,"we","soca",1))
#except Exception as e:
 #       print "Impossibile inserire il dato",e

# crea la nuova tabella
db.create_all()

# aggiunge alla tabella user il dato
db.session.add(user_("administrator",bycrypt_on_pass_user.generate_password_hash('binocchio1977'),"alessio.bino@gmail.com","alessio","bino",profile_type_.name))
#db.session.query(gauge_).filter_by(id_gauge=1).delete()
#db.session.add(profile_type_(""))
#db.session.commit()








