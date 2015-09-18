__author__ = 'Alessio'

from project import db
from flask_login import UserMixin
from project import login_,principal_role
'''importa il login dall app principale'''

class Permisssion:
      VIEV = 0X01
      CHANGE = 0X08
      ADMINISTRATOR = 0x88

class profile_type_(db.Model):

    __tablename__ = "profile_type"

    id_role = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    permission = db.Column(db.Integer)
    id_user = db.relationship('user_', backref='profile_type')

    def __init__(self,name=None,permission=None):

             self.name = name
             self.permission = permission


    def __repr__(self):
         return "<name  {0}>".format(self.name)

    @staticmethod
    def insert_role():
        '''inserisci i profili direttamnte senza richiamarli tramite funzione '''
        profile = {
             'User':(Permisssion.VIEV),
             'Manager':(Permisssion.VIEV |
                       Permisssion.CHANGE),
             'Administrator':(0xff)
        }

        for r in profile:
           role = profile_type_.query.filter_by(name=r).first()
           print profile[r],r

        #    if role is None:
        #        role = profile_type_(name=r)
        #    role.permission = profile[r]
        #    db.session.add(role)
        # db.session.commit()




class gauge_(db.Model):

    __tablename__ = "gauge_select"

    ''' crea il modello per salvare i dati dei vari gauge
    '''
    id_gauge = db.Column(db.Integer, primary_key=True)
    name_gauge = db.Column(db.String)
    name_gauge_change = db.Column(db.String)
    gauge_choiche= db.Column(db.Boolean)
    id_ = db.Column(db.Integer, db.ForeignKey('user.id_user'))

    def __init__(self,name_gauge=None,name_gauge_change=None,gauge_choiche=None,id_=None):

        """

        :type self: object
        """
        self.name_gauge = name_gauge
        self.name_gauge_change = name_gauge_change
        self.gauge_choiche = gauge_choiche
        self.id_ = id_

    def __repr__(self):
        return "<name  {0}>".format(self.name_gauge)

class user_(db.Model,UserMixin):
    ''' creazione del modello per salvare i dati
    '''
    __tablename__ = "user"

    id_user = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=True ,nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    role = db.Column(db.String, db.ForeignKey('profile_type.name'))
    gauge_ch = db.relationship('gauge_', backref='user')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id_user)

    def __init__(self ,user=None,password=None,email=None,first_name=None,last_name=None,role=None):
        '''
        :param user:
        :param password:
        :param email:
        :param first_name:
        :param last_name:
        :param role:
        :return:
        '''
        self.user = user
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.role = role

    def __repr__(self):
        return "<name  {0}>".format(self.user)

    @login_.user_loader
    def load_user(id_user=None):
        '''query per ritornare user id della tabella user_'''
        return user_.query.get(int(id_user))

