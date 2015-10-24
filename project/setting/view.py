__author__ = 'Alessio'

from functools import wraps
from datetime import datetime
from flask import render_template, redirect, url_for, session, flash, request,Blueprint,Response
from project import db,admin_manager_permission
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
@admin_manager_permission.require(http_exception=403)
def setting_():
    d = []
    user_gauge_id = current_user.id_user
    gauge_user_user_id = gauge_.query.filter_by(id_=user_gauge_id).all()
    form = form_check_gauge(request.form)
    print len(gauge_user_user_id)
    for single_object_query_for_id in gauge_user_user_id:
        d.append(single_object_query_for_id)
    if len(gauge_user_user_id) !=0:
        if form.validate_on_submit():
             d[0].name_gauge_change = form.name_change_gauge_van.data
             d[0].gauge_choiche = form.name_checked_gauge_van.data
             d[1].name_gauge_change = form.name_change_gauge_vbn.data
             d[1].gauge_choiche = form.name_checked_gauge_vbn.data
             d[2].name_gauge_change = form.name_change_gauge_vcn.data
             d[2].gauge_choiche = form.name_checked_gauge_vcn.data
             for my_vale_change in d:
                 db.session.add(my_vale_change)
             db.session.commit()
             flash("update the gauge for user {}".format(current_user.user))
             return render_template('setting_.html',current_time = datetime.utcnow(),form=form)
        form.name_change_gauge_van.data =  d[0].name_gauge_change
        form.name_checked_gauge_van.data = d[0].gauge_choiche
        form.name_change_gauge_vbn.data = d[1].name_gauge_change
        form.name_checked_gauge_vbn.data = d[1].gauge_choiche
        form.name_change_gauge_vcn.data = d[2].name_gauge_change
        form.name_checked_gauge_vcn.data = d[2].gauge_choiche
        return render_template('setting_.html',current_time = datetime.utcnow(),form=form)
    if len(gauge_user_user_id) == 0:
        if form.validate_on_submit():
            complete_list_gauge_add = [gauge_(name_gauge=form.name_change_gauge_van.label.text,name_gauge_change=form.name_change_gauge_van.data,
                                  gauge_choiche=form.name_checked_gauge_van.data,id_=user_gauge_id),
                            gauge_(name_gauge=form.name_change_gauge_vbn.label.text,name_gauge_change=form.name_change_gauge_vbn.data,
                                  gauge_choiche=form.name_checked_gauge_vbn.data,id_=user_gauge_id),
                          gauge_(name_gauge=form.name_change_gauge_vcn.label.text,name_gauge_change=form.name_change_gauge_vcn.data,
                                 gauge_choiche=form.name_checked_gauge_vcn.data,id_=user_gauge_id)]
            db.session.add_all(complete_list_gauge_add)
            db.session.commit()
            return render_template('setting_.html',form=form,current_time=datetime.utcnow())
    return render_template('setting_.html',form=form,current_time=datetime.utcnow())
