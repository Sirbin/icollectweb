__author__ = 'Alessio'

from flask_wtf import Form
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import StringField ,BooleanField,SubmitField,PasswordField,SelectField,HiddenField
from wtforms.validators import DataRequired,Required,Length,EqualTo,Optional,Email,InputRequired



# class form_check_gauge(Form):
#     ''' form per collegamento gauge'''
#     name_change_gauge_van = StringField("Gauge_VaN")
#     name_checked_gauge_van = BooleanField("Gauge_ckd_VaN")
#
#
#     name_change_gauge_vbn = StringField("Gauge_VbN",validators=[Optional()])
#     name_checked_gauge_vbn = BooleanField("Gauge_ckd_VbN",validators=[Optional()])





# class login_users(Form):
#     ''' form per login
#     '''
#     user_login = StringField('user', validators=[DataRequired(),Length(min=5,max=40)])
#     user_password = PasswordField('password', validators=[DataRequired(),Length(min=5,max=40)])
#
#
# class register_user(Form):
#     ''' registrazione utenti
#     '''
#     user = StringField('user',validators=[DataRequired(),Length(min=6,max=40)])
#     password = PasswordField('password',validators=[DataRequired(),Length(min=8,max=40)])
#     confirm = PasswordField('repear password',validators=[DataRequired(),EqualTo('password',message='password must math')])
#     email = StringField('email',validators=[DataRequired(), Email(),Length(min=6,max=40)])
#     first_name = StringField('first name',validators=[DataRequired()])
#     last_name = StringField('last name',validators=[DataRequired()])
#     select_profile = SelectField('Select Profile',choices=[('admin','admin'),('users','user'),('viewer','viewer')],validators=[DataRequired()])