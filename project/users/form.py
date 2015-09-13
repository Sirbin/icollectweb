__author__ = 'Alessio'

from flask_wtf import Form
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import StringField ,BooleanField,SubmitField,PasswordField,SelectField,HiddenField
from wtforms.validators import DataRequired,Required,Length,EqualTo,Optional,Email,InputRequired
from project import model_,db

def get_query():
    my_db =  db.session.query(model_.profile_type_.name).all()
    return  my_db

class login_users(Form):
    ''' form per login
    '''
    user_login = StringField('user', validators=[DataRequired(),Length(min=5,max=40)])
    user_password = PasswordField('password', validators=[DataRequired(),Length(min=5,max=40)])


class register_user(Form):
    ''' registrazione utenti
    '''
    user = StringField('user',validators=[DataRequired(),Length(min=6,max=40)])
    password = PasswordField('password',validators=[DataRequired(),Length(min=8,max=40)])
    confirm = PasswordField('repear password',validators=[DataRequired(),EqualTo('password',message='password must math')])
    email = StringField('email',validators=[DataRequired(), Email(),Length(min=6,max=40)])
    first_name = StringField('first name',validators=[DataRequired()])
    last_name = StringField('last name',validators=[DataRequired()])
    select_profile = SelectField('Select Profile',choices=[(f.name,f.name) for f in get_query()],validators=[DataRequired()])
    #select_profile = QuerySelectField('Select Profile',query_factory= get_query())


if __name__ == '__main__':
  pass
     #('Admin','Admin'),('Users','User'),('Manager','Manager')