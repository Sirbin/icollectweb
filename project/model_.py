__author__ = 'Alessio'

from project import db

class gauge_(db.Model):

    __tablename__ = "gauge_select"

    ''' crea il modello per salvare i dati dei vari gauge
    '''
    id_gauge = db.Column(db.Integer, primary_key=True)
    name_gauge = db.Column(db.String,unique=True)
    name_gauge_change = db.Column(db.String)
    gauge_choiche= db.Column(db.String)
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

class user_(db.Model):
    ''' creazione del modello per salvare i dati
    '''
    __tablename__ = "user"

    id_user = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=True ,nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    profile_type = db.Column(db.String)
    gauge_ch = db.relationship('gauge_', backref='poster')


    def __init__(self ,user=None,password=None,email=None,first_name=None,last_name=None,profile_type=None):
        '''
        :param user:
        :param password:
        :param email:
        :param first_name:
        :param last_name:
        :param profile_type:
        :return:
        '''
        self.user = user
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.profile_type = profile_type

    def __repr__(self):
        return "<name  {0}>".format(self.user)
