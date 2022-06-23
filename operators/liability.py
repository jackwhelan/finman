import requests
from datetime import datetime

from classes.Liability import Liability
from etc.config import ConfigHandler
from etc.exceptions import CreateLiabilityException

config = ConfigHandler()

def create_liability(name: str, description: str, value: float):
    Liability(name, description, value, datetime.now())

    payload = {
        "name": name,
        "description": description,
        "value": value,
        "last_updated": str(datetime.now())
    }

    response = requests.post(f'{config["connection_uri"]}/finman/liability', json=payload)
    return response.json()

def get_liability(oid):
    # TODO: Refactor
    if oid is not None:
        response = requests.get(f'{config["connection_uri"]}/finman/liability?oid={oid}')
        return { 'Liability': response.json()['response'] }
    liabilities = []
    response = requests.get(f'{config["connection_uri"]}/finman/liability')
    for liability in response.json()['response']:
        liabilities.append(Liability(liability['name'], liability['description'], liability['value'], liability['last_updated'], liability['_id']).__dict__)
    return { 'Liabilities': liabilities }

def update_liability(oid, updates: dict):
    if not oid:
        raise CreateLiabilityException('Could not update Liability without object ID. Please pass a valid liability oid as a url argument')

    # The reason for creating a new payload instead of directly using the updates dictionary is to enforce only modifying
    # existing Liability fields rather than allowing the API to add non existing values using a patch request.
    payload = {}

    if 'name' in updates:
        payload['name'] = updates['name']

    if 'description' in updates:
        payload['description'] = updates['description']

    if 'value' in updates:
        payload['value'] = updates['value']

    payload['last_updated'] = str(datetime.now())

    response = requests.patch(f'{config["connection_uri"]}/finman/liability?oid={oid}', json=payload)
    return { 'Liability': response.json() }

def delete_liability(oid):
    if oid is not None:
        response = requests.delete(f'{config["connection_uri"]}/finman/liability?oid={oid}')
        return response.json()
