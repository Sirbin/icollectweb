__author__ = 'Alessio'

# Import
from datetime import datetime
from functools import wraps
from flask import render_template, redirect, url_for,flash, request, Blueprint,current_app
from sqlalchemy.exc import IntegrityError
from .form import register_user , login_users
from project.model_ import user_
from project import db,bycrypt_on_pass_user,app
from project.Loggin_Debug import Logging
from flask_login import login_user,logout_user,login_required,current_user,session
from flask.ext.principal import identity_changed,Identity,AnonymousIdentity


#config
users_for_blueprint = Blueprint('user',__name__)

# Function error field login and edit user
def flask_error(form):
    for field, errors in form.error.itemes():
        for error in errors:
            flash('Error in the %s field - %s' % (getattr(form, field).label.text, error), 'error')



@users_for_blueprint.route('/', methods=['GET','POST'])
def login_():
    error = None
    form = login_users()
    if form.validate_on_submit():
         user = user_.query.filter_by(user=form.user_login.data).first()
         if user is not None and bycrypt_on_pass_user.check_password_hash(user.password,form.user_password.data):
            login_user(user,form.user_remember.data)
            identity = Identity(form.user_login.data)
            identity_changed.send(app,identity=identity)
            flash("you are logged Welcome %s" % current_user.user)
            now_time =datetime.now()
            user_logging = Logging(user_connect_=None)
            user_logging.create_login_info(current_user.user,now_time.strftime('%d-%m-%Y %H-%M-%S'), request.url)
            return redirect(request.args.get('next') or url_for('general.dashboard_'))
         error = "Invalid User or Password"
    return render_template('Login.html',error=error,form=form)


 # Funzione Logout
@users_for_blueprint.route('/logout')
@login_required
def logout_():
    now_time =datetime.now()
    user_logging = Logging(user_connect_=None)
    user_logging.create_logout_info(current_user.user, now_time.strftime('%d-%m-%Y %H-%M-%S'))
    flash('Goodbye %s' % current_user.user)
    logout_user()
    for key in ('identity.id','identity.auth_type'):
        session.pop(key,None)
    return redirect(url_for('user.login_'))

@users_for_blueprint.route('/dashboard/users/new_user', methods=['GET', 'POST'])
@login_required
def new_users():
    error = None
    form = register_user(request.form)
    #if request.method == "POST":
    if form.validate_on_submit():
            new_user = user_(form.user.data,bycrypt_on_pass_user.generate_password_hash(form.password.data), form.email.data, form.first_name.data,
                             form.last_name.data, str(form.select_profile.data))
            try:
                db.session.add(new_user)
                db.session.commit()
                flash('New user register')
                return redirect(url_for('user.user_page'))
            except IntegrityError:
                error = "username and/or email exist"
                #return  redirect(url_for('new_users'))
                return render_template('new_users.html', form=form, error=error,
                                       current_time=datetime.utcnow())
    return render_template('new_users.html', form=form, error=error,
                           current_time=datetime.utcnow())

@users_for_blueprint.route('/dashboard/users/edit/<useredit>', methods=['POST', 'GET'])
@login_required
def edit_users(useredit):
    error = None
    form = register_user(request.form)
    useredit_change = useredit
    query_for_change_user = user_.query.filter_by(user=useredit_change)
    if request.method == "POST":
        if form.validate_on_submit():
            try:
                db.session.query(user_).filter_by(user=useredit_change).update(
                    {"user": form.user.data, "profile_type": form.select_profile.data, "password": bycrypt_on_pass_user.generate_password_hash(form.password.data),
                     "email": form.email.data, "first_name": form.first_name.data, "last_name": form.last_name.data})
                db.session.commit()
                flash('User {0} Upadate'.format(form.user.data))
                return redirect(url_for('user.user_page'))
            except IntegrityError:
                error = "username and/or email are exist"
                return render_template('edit_user.html', useredit_change=query_for_change_user, form=form, error=error,
                                        current_time=datetime.utcnow())
    return render_template('edit_users.html', user_change=query_for_change_user, form=form,
                           error=error, current_time=datetime.utcnow())


@users_for_blueprint.route('/dashboard/users/<usersdel>')
@login_required
def delete_users(usersdel):
        delete_us = usersdel
        db.session.query(user_).filter_by(user=delete_us).delete()
        db.session.commit()
        flash('users delete')
        return redirect(url_for('user.user_page'))

@users_for_blueprint.route('/dashboard/users')
@login_required
def user_page():
    users_site = db.session.query(user_).order_by(user_.id_user)
    return render_template('users.html', users=users_site, current_time=datetime.utcnow())
