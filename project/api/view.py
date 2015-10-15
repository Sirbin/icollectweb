__author__ = 'Alessio'

from project import db
from flask import Blueprint,flash,jsonify

from project.model_ import user_

#blueprint
api_blueprint = Blueprint('api',__name__)

# Function error field login and edit user
def flask_error(form):
    for field, errors in form.error.itemes():
        for error in errors:
            flash('Error in the %s field - %s' % (getattr(form, field).label.text, error), 'error')


@api_blueprint.route('/api/v1/user')
def api_user():
    result = db.session.query(user_).limit(3).offset(0).all()
    json_result=[]
    for res in result:
        data = {
            'user' : res.user,
            'email': res.email,
            'first':res.first_name,
            'last' : res.last_name,
            'role:':res.role
        }
        json_result.append(data)
    return  jsonify(items=json_result)

# @api_blueprint.route('/api/v1/user/<userdit>')
# def api_edit_user(userdit):
#     result = db.session.query(user_).filter_by(user=userdit).first()
#     json_result = {
#         'user':result.user,
#         'email':result.email,
#         'first_name':result.first_name,
#         'last_name':result.last_name,
#         'role':result.role
#         }
#     return jsonify(items=json_result)

@api_blueprint.route('/api/v1/user/<userdit>')
def api_edit_user(userdit):
    result = db.session.query(user_).filter_by(user=userdit).first()
    if result:
        json_result = {
        'user':result.user,
        'email':result.email,
        'first_name':result.first_name,
        'last_name':result.last_name,
        'role':result.role
        }
        return jsonify(items=json_result)
    else:
        result = {"error" : "element not exist" }
        return jsonify(result)