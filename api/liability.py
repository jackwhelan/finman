from flask import Blueprint, request

from operators.liability import create_liability, get_liability, update_liability, delete_liability

liability_routes = Blueprint('liability_routes', __name__)

@liability_routes.route('/liability', methods = ['POST'])
def create():
    req = request.get_json()
    return create_liability(req['name'], req['description'], req['value'])

@liability_routes.route('/liability', methods = ['GET'])
def read():
    return get_liability(request.args.get('oid'))

@liability_routes.route('/liability', methods = ['PATCH'])
def update():
    updates = request.get_json()
    return update_liability(request.args.get('oid'), updates)

@liability_routes.route('/liability', methods = ['DELETE'])
def delete():
    return delete_liability(request.args.get('oid'))
