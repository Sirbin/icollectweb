__author__ = 'Alessio'

from functools import wraps
from datetime import datetime
from flask import render_template, redirect, url_for, session, flash, request,Blueprint,Response
from project import db,admin_permission
from .form import form_check_gauge
from project.model_ import gauge_
from flask_login import login_required,current_user



#config
blueprint_setting = Blueprint('setting',__name__)

#Function error field login and edit user
def flask_error(form):
    for field, errors in form.error.itemes():
        for error in errors:
            flash('Error in the %s field - %s' % (getattr(form, field).label.text, error), 'error')





@blueprint_setting.route("/dashboard/setting", methods=['GET', 'POST'])
@login_required
@admin_permission.require(http_exception=403)
def setting_():
    user_gauge_id = current_user.id_user
    gauge_user_user_id = gauge_.query.filter_by(id_=user_gauge_id).first()
    form = form_check_gauge(request.form)
    if request.method == "POST":
        if gauge_user_user_id is None:
             gauge_select = gauge_(form.name_change_gauge_van.label.text, form.name_change_gauge_van.data,
                               form.name_checked_gauge_van.data, user_gauge_id)
             db.session.add(gauge_select)
             db.session.commit()
             flash("Saved")
             return render_template('setting_.html', form=form, current_time=datetime.utcnow(),name_controll = gauge_user_user_id)
        elif user_gauge_id == gauge_user_user_id.id_:
                print form.name_checked_gauge_van.data
                print form.name_change_gauge_van.data
                gauge_.query.filter_by(id_=user_gauge_id).update(
                     {"name_gauge_change": form.name_change_gauge_van.data, "gauge_choiche": form.name_checked_gauge_van.data})
                db.session.commit()
                flash("Saved")
                return render_template('setting_.html', form=form, current_time=datetime.utcnow(),name_controll = gauge_user_user_id)
    return render_template('setting_.html', form=form, current_time=datetime.utcnow(),name_controll = gauge_user_user_id)
