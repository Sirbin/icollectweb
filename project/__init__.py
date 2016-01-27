__author__ = 'Alessio'

from datetime import *

from flask import Flask,render_template,request, session, current_app
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask.ext.bcrypt import Bcrypt
from flask_login import LoginManager,current_user
from flask_principal import Principal,Permission,RoleNeed,identity_loaded, UserNeed
from flask_mail import Mail


#monkey.patch_all()

app = Flask(__name__)


# application moment for time e location
moment = Moment(app)

# configuration file
app.config.from_pyfile('config_.py')

# applications Socketio
socketio = SocketIO(app)

# password crypt
bycrypt_on_pass_user = Bcrypt(app)

# database
db = SQLAlchemy(app)

#Login Manager
login_ = LoginManager()
login_.session_protection =     None
login_.login_view = 'user.login_'
login_.init_app(app)

#Principal Role
principal_role = Principal(app)

admin_permission = Permission(RoleNeed('Admin'))

admin_manager_permission = Permission(RoleNeed('Admin'),RoleNeed('Manager'))

user_permission = Permission(RoleNeed('User'))

#Mail

server_mail = Mail(app)


from setting.view import blueprint_setting
from general.view import blueprint_general
from broker.view import blueprint_mqtt_data
from users.view import users_for_blueprint
from api.view import api_blueprint

#register
app.register_blueprint(blueprint_setting)
app.register_blueprint(blueprint_general)
app.register_blueprint(blueprint_mqtt_data)
app.register_blueprint(users_for_blueprint)
app.register_blueprint(api_blueprint)



@identity_loaded.connect_via(app)
def on_identity_loader(sender,identity):
    identity.id = current_user.id_user
    identity.user = current_user.user

    if hasattr(current_user,'id'):
        identity.provides.add(UserNeed,(current_user.id))

    if hasattr(current_user,'role'):
        identity.provides.add(RoleNeed(current_user.role))


#funzioni errori pagina
@app.errorhandler(404)
def page_not_found(error):
    if app.debug is not True:
        now_time = datetime.now()
        r = request.url
        with open('error.log','a') as f:
            current_time = now_time.strftime('%d-%m-%Y %H-%M-%S')
            f.write("error 404, {0} , {1}\n".format(current_time,r))
    return render_template('404.html', current_time=datetime.utcnow()), 404

@app.errorhandler(500)
def server_internal_error(error):
    db.session.rollback()
    if app.debug is not True:
        now_time = datetime.now()
        r = request.url
        with open('error.log','a') as  f:
            current_time = now_time.strftime('%d-%m-%Y %H-%M-%S')
            f.write("error 500, {0}, {1}".format(current_time,r))
    return render_template('500.html', current_time=datetime.utcnow()), 500

@app.errorhandler(401)
def admin_permited_error(e):
    error = ('Your current identity is {user}. You need special privileges to access this page') \
             .format(user=current_user.user)
    return render_template('dashboard_.html',error=error, current_time = datetime.utcnow())

@app.errorhandler(403)
def prova_errore(e):
    error = ('Your current identity is {user}. You need special privileges to access this page') \
             .format(user=current_user.user)
    session['redirect_url']=request.url
    return render_template('users.html', error=error , current_time = datetime.utcnow())

'''if want send a single parameters on template , create a single functions '''
def breadcrumbss(my_url):
           bread_crumbs =[]
           sr_url = my_url.split('/')
           url = '' 
           for brcr in sr_url:
               if brcr !='':
                url = '%s/%s' % (url,brcr)
                bread_crumbs_dict =  {'brcr':brcr,"url":url}
                bread_crumbs.append(bread_crumbs_dict)
           return dict(breadcrumbs= bread_crumbs)

# send to template
app.jinja_env.globals.update(breadcrumbs=breadcrumbss)

if __name__ == '__main__':
    pass