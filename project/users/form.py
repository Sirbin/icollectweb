__author__ = 'Alessio'

from flask_wtf import Form
from wtforms import StringField ,BooleanField,PasswordField,SelectField
from wtforms.validators import DataRequired,Length,EqualTo,Email,ValidationError
from project import db,model_,login_
from project.model_ import user_

def get_query():
    my_db =  db.session.query(model_.profile_type_.name).all()
    return  my_db

class login_users(Form):
    '''
    form per login
    '''
    user_login = StringField('user', validators=[DataRequired(),Length(min=5,max=40)])
    user_password = PasswordField('password', validators=[DataRequired(),Length(min=5,max=40)])
    user_remember = BooleanField('Remember me')


class register_user(Form):
    '''
    edit user
    '''
    user = StringField('user',validators=[DataRequired(),Length(min=6,max=40)])
    password = PasswordField('password',validators=[DataRequired(),Length(min=8,max=40)])
    confirm = PasswordField('repear password',validators=[DataRequired(),EqualTo('password',message='password must math')])
    email = StringField('email',validators=[DataRequired(), Email(),Length(min=6,max=40)])
    first_name = StringField('first name',validators=[DataRequired()])
    last_name = StringField('last name',validators=[DataRequired()])
    select_profile = SelectField('Select Profile',choices=[(f.name,f.name) for f in get_query()],validators=[DataRequired()])


    def __init__(self,username=None,*args, **kwargs):
        super(register_user,self).__init__(*args,**kwargs)

        self.username = username

    def validate_email(self,field):
         email_control = user_.query.filter_by(email=field.data).first()
         print "my email",email_control
         if field.data != self.username.email and email_control:
            raise ValidationError ('Email already exist')

    def validate_user(self,field):
        user_control = user_.query.filter_by(user=field.data).first()
        print "my user",user_control
        if field.data != self.username.user and  user_control:
            raise ValidationError('User already exist')


class new_register_user(Form):
     '''registration new user'''

     user = StringField('user',validators=[DataRequired(),Length(min=6,max=40)])
     password = PasswordField('password',validators=[DataRequired(),Length(min=8,max=40)])
     confirm = PasswordField('repear password',validators=[DataRequired(),EqualTo('password',message='password must math')])
     email = StringField('email',validators=[DataRequired(), Email(),Length(min=6,max=40)])
     first_name = StringField('first name',validators=[DataRequired()])
     last_name = StringField('last name',validators=[DataRequired()])
     select_profile = SelectField('Select Profile',choices=[(f.name,f.name) for f in get_query()],validators=[DataRequired()])

     def validate_email(self,field):
        email_control = user_.query.filter_by(email=field.data).first()
        if email_control:
            raise ValidationError ('Email already exist')

     def validate_user(self,field):
        user_control = user_.query.filter_by(user=field.data).first()
        if user_control:
            raise ValidationError('User already exist')
