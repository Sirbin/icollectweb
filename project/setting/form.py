__author__ = 'Alessio'

from flask_wtf import Form
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import StringField ,BooleanField,SubmitField,PasswordField,SelectField,HiddenField
from wtforms.validators import DataRequired,Required,Length,EqualTo,Optional,Email,InputRequired


class form_check_gauge(Form):
    ''' form per collegamento gauge'''
    name_change_gauge_van = StringField("Gauge_VaN")
    name_checked_gauge_van = BooleanField("Gauge_ckd_VaN")

    name_change_gauge_vbn = StringField("Gauge_VbN")
    name_checked_gauge_vbn = BooleanField("Gauge_ckd_VbN")

    name_change_gauge_vcn = StringField("Gauge_VcN")
    name_checked_gauge_vcn = BooleanField("Gauge_ckd_VcN")

    name_change_gauge_ian = StringField("Gauge_IaN")
    name_checked_gauge_ian = BooleanField("Gauge_ckd_IaN")

    name_change_gauge_ibn = StringField("Gauge_IbN")
    name_checked_gauge_ibn = BooleanField("Gauge_ckd_IbN")

    name_change_gauge_icn = StringField("Gauge_IcN")
    name_checked_gauge_icn = BooleanField("Gauge_ckd_IcN")

    name_change_gauge_phase = StringField("Phase")
    name_checked_gauge_phase = BooleanField("Gauge_Phase")


    def __init__(self, username_id=None,*args,**kwargs):
        super(form_check_gauge,self).__init__(*args,**kwargs)

        self.username_id = username_id

