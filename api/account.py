import logging
from flask import Blueprint, request
import requests

from operators.account import create_account, get_account, update_account, delete_account
from etc.config import ConfigHandler

account_routes = Blueprint('api_version', __name__)

config = ConfigHandler()

@account_routes.route('/account', methods = ['POST'])
def create():
    req = request.get_json()
    payload = create_account(req['person_id'], req['account_description'], req['balance'],
                             req['assets'], req['liabilities'], req['transaction_history'],
                             req['scheduled_transactions'])
    requests.post(config['connection_uri'], data=payload)

@account_routes.route('/account', methods = ['GET'])
def read():
    response = get_account(request.args.get('oid'))
    return response

@account_routes.route('/account', methods = ['PATCH'])
def update():
    payload = update_account(request.get_json())
    requests.patch(config['connection_uri'], params=request.args)

@account_routes.route('/account', methods = ['DELETE'])
def delete():
    requests.delete(config['connection_uri'], params=request.args)
