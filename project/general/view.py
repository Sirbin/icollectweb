__author__ = 'Alessio'

from datetime import datetime
from flask import render_template, redirect, url_for, flash, Blueprint,request
from project.json_conf_ import create_tenant_building,create_json_table,create_json_building,create_json_tne
from project import db,app
from project.model_ import gauge_ ,user_
from flask_login import login_required,current_user,confirm_login,login_user
from flask.ext.principal import identity_changed,Identity
#config
blueprint_general = Blueprint('general',__name__ )

#configuration Json
json_tne_number = create_json_tne()
json_building = create_json_building()
json_table_meter_value = create_json_table()
json_tenant_building = create_tenant_building()


#Function error field login and edit user
def flask_error(form):
     for field, errors in form.error.itemes():
         for error in errors:
             flash('Error in the %s field - %s' % (getattr(form, field).label.text, error), 'error')


@blueprint_general.route('/confirm/<id>')
@login_required
def confirm_email(id):
    id_user__ = id
    user__mail_ = user_.query.filter_by(id_user=id_user__).first()
    login_user(user__mail_,force=True)
    identity = Identity(user__mail_.user)
    identity_changed.send(app,identity=identity)
    flash('User Confirm')
    return render_template('Confirm_user_id.html', current_time=datetime.utcnow())


# Pagina Principale dashbord da creare
@blueprint_general.route('/dashboard')
@login_required
def dashboard_():
    return render_template('dashboard_.html',current_time=datetime.utcnow())


@blueprint_general.route('/dashboard/building')
@login_required
def building_():
    if json_building != False:
        return render_template('building.html', json_building=json_building, json_tne_number=json_tne_number,
                               json_table_meter_value=json_table_meter_value,
                               json_tenant_building=json_tenant_building,
                               current_time=datetime.utcnow())
    return redirect(url_for('dashboard_'))



@blueprint_general.route('/dashboard/tenant')
@login_required
def tenant_():
    return render_template("tenant.html", json_tenant_building=json_tenant_building,
                           json_building=json_building, current_time=datetime.utcnow())


@blueprint_general.route("/dashboard/tenant/<tenant>")
@login_required
def tenant_name_(tenant):
    if json_building != False:

        return render_template('tenant_name.html', tenant=tenant,json_tenant_building=json_tenant_building,
                               current_time=datetime.utcnow(),json_building=json_building)
    return redirect(url_for('tenant.html'))

@blueprint_general.route("/dashboard/meters")
@login_required
def meters_():
    if json_building != False:
        return render_template('meters.html', json_tenant_building=json_tenant_building,
                               json_table_meter_value=json_table_meter_value,
                               json_building=json_building, current_time=datetime.utcnow())

@blueprint_general.route('/dashboard/prova')
@login_required
def gauge_prova():
        value_tot = {}
        tne = json_table_meter_value
        user_gauge_id = current_user.id_user
        gauge_user_user_id = db.session.query(gauge_).filter_by(id_=user_gauge_id)
        for t in gauge_user_user_id:
            print "valore default %s" % t
            print t.id_, t.name_gauge_change, t.gauge_choiche
            value_tot[t.name_gauge] = dict(name_gauge_choiche = t.gauge_choiche, name_gauge_change = t.name_gauge_change)
        if len(value_tot) != 0:
            return render_template('prova.html', tne_id = json_table_meter_value,current_time=datetime.utcnow(),scelta_van =value_tot)
        return render_template('prova.html', current_time= datetime.utcnow(),scelta_van = value_tot)
