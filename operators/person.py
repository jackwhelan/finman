import json
import requests
from bson.objectid import ObjectId

from exceptions import CreatePersonException

def create_person(first_name: str, last_name: str):
    if not first_name.isalpha():
        raise CreatePersonException('First name must only contain letters.')
    
    if not last_name.isalpha():
        raise CreatePersonException('Last name must only contain letters.')
    
    if not len(first_name) > 1 and len(first_name <= 30):
        raise CreatePersonException('First name must be between 2 and 30 characters in length.')
    
    if not len(last_name) > 1 and len(last_name <= 30):
        raise CreatePersonException('Last name must be between 2 and 30 characters in length.')
    
    payload = {
        "firstName": first_name,
        "lastName": last_name
    }
    
    response = requests.post(f'http://data-access:5000/finman/person', json=json.dumps(payload))
    return { 'response': response.json() }

def get_person(oid: ObjectId):
    if oid:
        response = requests.get(f'http://data-access:5000/finman/person', params={'oid': oid})
    else:
        response = requests.get(f'http://data-access:5000/finman/person')
    # retrieved_account = Account(response['owner'], response['description'], response['balance'], response['assets'],
    #                             response['liabilities'], response['transaction_history'], response['scheduled_transactions'])
    return { 'response': response.json() }

def update_person():
    pass

def delete_person():
    pass
