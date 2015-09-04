__author__ = 'Alessio'

# Import
from datetime import datetime
from functools import wraps
from flask import render_template, redirect, url_for, session, flash, request, Blueprint
from sqlalchemy.exc import IntegrityError
from .form import register_user , login_users
from project.model_ import user_
from project import db

#config
users_for_blueprint = Blueprint('user',__name__)




# Function help
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login_'))
    return wrap

# Function error field login and edit user
def flask_error(form):
    for field, errors in form.error.itemes():
        for error in errors:
            flash('Error in the %s field - %s' % (getattr(form, field).label.text, error), 'error')

 # Funzione Users Login
@users_for_blueprint.route('/', methods=['GET', 'POST'])
def login_():
    error = None
    form = login_users(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = user_.query.filter_by(user=request.form['user_login']).first()
            if user is not None and user.password == request.form['user_password']:
                session['logged_in'] = True
                session['user_id'] = user.id_user
                session['user'] = user.user
                session['profile'] = user.profile_type
                flash("you are logged Welcome %s" % session['user'])
                return render_template('dashboard_.html', username=session['user'], current_time=datetime.utcnow())
            else:
                error = "Invalid User or Password"
        else:
            error = "Both Field are required"
    return render_template("Login.html", form=form, error=error)


 # Funzione Logout
@users_for_blueprint.route('/logout')
@login_required
def logout_():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    session.pop('user',None)
    session.pop('profile',None)
    flash('Goodbye')
    return redirect(url_for('login_'))

@users_for_blueprint.route('/dashboard/users/new_user', methods=['GET', 'POST'])
@login_required
def new_users():
    error = None
    form = register_user(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            new_user = user_(form.user.data, form.password.data, form.email.data, form.first_name.data,
                             form.last_name.data, str(form.select_profile.data))
            try:
                db.session.add(new_user)
                db.session.commit()
                flash('New user register')
                return redirect(url_for('users.user_page'))
            except IntegrityError:
                error = "username and/or email exist"
                return render_template('new_users.html', form=form, error=error, username=session['user'],
                                       current_time=datetime.utcnow())
    return render_template('new_users.html', form=form, error=error, username=session['user'],
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
                    {"user": form.user.data, "profile_type": form.select_profile.data, "password": form.password.data,
                     "email": form.email.data, "first_name": form.first_name.data, "last_name": form.last_name.data})
                db.session.commit()
                flash('User %s' % form.user.data, 'Update')
                return redirect(url_for('user_page'))
            except IntegrityError:
                error = "username and/or email are exist"
                return render_template('edit_user.html', useredit_change=query_for_change_user, form=form, error=error,
                                       usernam=session['user'], current_time=datetime.utcnow())
    return render_template('edit_users.html', user_change=query_for_change_user, form=form, username=session['user'],
                           error=error, current_time=datetime.utcnow())


@users_for_blueprint.route('/dashboard/users/<usersdel>')
@login_required
def delete_users(usersdel):
    error = None
    if session['profile'] == "admin":
        delete_us = usersdel
        db.session.query(user_).filter_by(user=delete_us).delete()
        db.session.commit()
        flash('users delete')
        return redirect(url_for('user_page'))
    else:
        flash('User {0} is not Administrator'.format(session['user']))
        return redirect(url_for('user_page'))

@users_for_blueprint.route('/dashboard/users')
@login_required
def user_page():
    users_site = db.session.query(user_).order_by(user_.id_user)
    return render_template('users.html', users=users_site, username=session['user'], current_time=datetime.utcnow())
