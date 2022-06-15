from flask import Blueprint, request

from operators.person import create_person, get_person, update_person, delete_person

person_routes = Blueprint('api_version', __name__)

@person_routes.route('/person', methods = ['POST'])
def create():
    req = request.get_json()
    return create_person(req['first_name'], req['last_name'])

@person_routes.route('/person', methods = ['GET'])
def read():
    return get_person(request.args.get('oid'))

@person_routes.route('/person', methods = ['PATCH'])
def update():
    updates = request.get_json()
    return update_person(request.args.get('oid'), updates)

@person_routes.route('/person', methods = ['DELETE'])
def delete():
    return delete_person(request.args.get('oid'))
