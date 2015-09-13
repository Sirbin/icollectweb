__author__ = 'Alessio'

from functools import wraps
from datetime import datetime
from flask import render_template, redirect, url_for, session, flash, request,Blueprint
from project import db
from .form import form_check_gauge
from project.model_ import gauge_
from sqlalchemy.exc import IntegrityError

#config
blueprint_setting = Blueprint('setting',__name__)

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

#Function error field login and edit user
def flask_error(form):
    for field, errors in form.error.itemes():
        for error in errors:
            flash('Error in the %s field - %s' % (getattr(form, field).label.text, error), 'error')

@blueprint_setting.route("/dashboard/setting", methods=['GET', 'POST'])
@login_required
def setting_():
    user_gauge_id = session['user_id']
    gauge_user_user_id = gauge_.query.filter_by(id_=user_gauge_id).first()
    form = form_check_gauge(request.form)
    if request.method == "POST":
        #gauge_user_user_id = gauge_.query.filter_by(id_=user_gauge_id).first()
        if gauge_user_user_id is None:
             gauge_select = gauge_(form.name_change_gauge_van.label.text, form.name_change_gauge_van.data,
                               form.name_checked_gauge_van.data, session['user_id'])
             try:
                 db.session.add(gauge_select)
                 db.session.commit()
                 flash("Gauge saved")
                 dato_van_check = form.name_checked_gauge_van.data
                 print "check_van", dato_van_check
                 id_van = form.name_checked_gauge_van.id
                 print "id _ck", id_van
                 print "txt", form.name_change_gauge_van.data
                 return render_template('setting_.html', form=form, username=session['user'], current_time=datetime.utcnow(),name_controll = gauge_user_user_id)
             except IntegrityError:
                 flash ("errore")
                 return redirect(url_for('setting_'))
        elif user_gauge_id == gauge_user_user_id.id_:
                print form.name_checked_gauge_van.data
                print form.name_change_gauge_van.data
                db.session.query(gauge_).update(
                     {"name_gauge_change": form.name_change_gauge_van.data, "gauge_choiche": form.name_checked_gauge_van.data})
                db.session.commit()
                flash("aggiornato")
                #return redirect(url_for('setting_'))
                return render_template('setting_.html', form=form, username=session['user'], current_time=datetime.utcnow(),name_controll = gauge_user_user_id)             #     #return render_template('setting_.html', form=form, username=session['user'], current_time=datetime.utcnow())
    return render_template('setting_.html', form=form, username=session['user'], current_time=datetime.utcnow(),name_controll = gauge_user_user_id)
