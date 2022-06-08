from flask import Blueprint, request
import requests

from operators.account import create_account, get_account, update_account, delete_account
from etc.config import ConfigHandler

account_api = Blueprint('api_version', __name__)

config = ConfigHandler()

@account_api.route('/account', methods = ['POST'])
def create():
    req = request.get_json()
    payload = create_account(req['person_id'], req['account_description'], req['balance'],
                             req['assets'], req['liabilities'], req['transaction_history'],
                             req['scheduled_transactions'])
    requests.post(config['connection_uri'], data=payload)

@account_api.route('/account', methods = ['GET'])
def read():
    requests.get(config['connection_uri'], params=request.args)

@account_api.route('/account', methods = ['PATCH'])
def update():
    payload = update_account(request.get_json())
    requests.patch(config['connection_uri'], params=request.args)

@account_api.route('/account', methods = ['DELETE'])
def delete():
    requests.delete(config['connection_uri'], params=request.args)


