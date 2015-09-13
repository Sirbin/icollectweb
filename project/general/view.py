__author__ = 'Alessio'

from datetime import datetime
from functools import wraps
from flask import render_template, redirect, url_for, session, flash, Blueprint
from project.json_conf_ import create_tenant_building,create_json_table,create_json_building,create_json_tne
from project import db
from project.model_ import gauge_

#config
blueprint_general = Blueprint('general',__name__)

#configuration Json
json_tne_number = create_json_tne()
json_building = create_json_building()
json_table_meter_value = create_json_table()
json_tenant_building = create_tenant_building()

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


# Pagina Principale dashbord da creare
@blueprint_general.route('/dashboard')
@login_required
def dashboard_():
    return render_template('dashboard_.html', username=session['user'], current_time=datetime.utcnow())


@blueprint_general.route('/dashboard/building')
@login_required
def building_():
    if json_building != False:
        return render_template('building.html', json_building=json_building, json_tne_number=json_tne_number,
                               json_table_meter_value=json_table_meter_value,
                               json_tenant_building=json_tenant_building, username=session['user'],
                               current_time=datetime.utcnow())
    return redirect(url_for('dashboard_'))



@blueprint_general.route('/dashboard/tenant')
@login_required
def tenant_():
    return render_template("tenant.html", json_tenant_building=json_tenant_building,
                           json_building=json_building, username=session['user'], current_time=datetime.utcnow())


@blueprint_general.route("/dashboard/tenant/<tenant>")
@login_required
def tenant_name_(tenant):
    if json_building != False:
        return render_template('tenant_name.html', tenant=tenant, username=session['user'],
                               current_time=datetime.utcnow())
    return redirect(url_for('tenant.html'))

@blueprint_general.route("/dashboard/meters")
@login_required
def meters_():
    if json_building != False:
        return render_template('meters.html', json_tenant_building=json_tenant_building,
                               json_table_meter_value=json_table_meter_value,
                               json_building=json_building, username=session['user'], current_time=datetime.utcnow())

@blueprint_general.route('/dashboard/prova')
@login_required
def gauge_prova():
        user_gauge_id = session['user_id']
        gauge_user_user_id = db.session.query(gauge_).filter_by(id_=user_gauge_id)
        if gauge_user_user_id is not None:
            for t in gauge_user_user_id:
                print t.id_, t.name_gauge_change, t.gauge_choiche
                value_tot = {"id":t.id_ ,"name":t.name_gauge_change,"choice":t.gauge_choiche}
            return render_template('prova.html',username=session['user'], current_time=datetime.utcnow(),scelta_van =t.gauge_choiche)
        return redirect(url_for('dashboard_'))