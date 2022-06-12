import logging
from flask import Blueprint, request
import requests
import json

from operators.person import create_person, get_person, update_person, delete_person
from etc.config import ConfigHandler

person_routes = Blueprint('api_version', __name__)

config = ConfigHandler()

@person_routes.route('/person', methods = ['POST'])
def create():
    req = request.get_json()
    response = create_person(req['first_name'], req['last_name'])
    return response

@person_routes.route('/person', methods = ['GET'])
def read():
    response = get_person(request.args.get('oid'))
    return response

@person_routes.route('/person', methods = ['PATCH'])
def update():
    updates = request.get_json()
    response = update_person(request.args.get('oid'), updates)
    return response

@person_routes.route('/person', methods = ['DELETE'])
def delete():
    requests.delete(config['connection_uri'], params=request.args)
