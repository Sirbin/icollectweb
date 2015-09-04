__author__ = 'Alessio'

from flask_wtf import Form
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import StringField ,BooleanField,SubmitField,PasswordField,SelectField,HiddenField
from wtforms.validators import DataRequired,Required,Length,EqualTo,Optional,Email,InputRequired


class form_check_gauge(Form):
    ''' form per collegamento gauge'''
    name_change_gauge_van = StringField("Gauge_VaN")
    name_checked_gauge_van = BooleanField("Gauge_ckd_VaN")


    name_change_gauge_vbn = StringField("Gauge_VbN",validators=[Optional()])
    name_checked_gauge_vbn = BooleanField("Gauge_ckd_VbN",validators=[Optional()])