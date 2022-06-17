import requests

from classes.Person import Person
from etc.config import ConfigHandler

config = ConfigHandler()

def create_person(first_name: str, last_name: str):
    Person(first_name, last_name, [], [])

    payload = {
        "first_name": first_name,
        "last_name": last_name,
        "assets": [],
        "liabilities": []
    }

    response = requests.post(f'{config["connection_uri"]}/finman/person', json=payload)
    return response.json()

def get_person(oid):
    # TODO: Refactor
    if oid is not None:
        response = requests.get(f'{config["connection_uri"]}/finman/person?oid={oid}')
        return { 'Person': response.json()['response'] }
    people = []
    response = requests.get(f'{config["connection_uri"]}/finman/person')
    for person in response.json()['response']:
        people.append(Person(person['first_name'], person['last_name'], person['assets'], person['liabilities'], person['_id']).__dict__)
    return { 'People': people }

def update_person(oid, updates: dict):
    if not oid:
        return {
            'status': '404',
            'message': 'Could not update Person without object ID. Please pass a valid Person oid as a url argument'
        }, 404
    
    existing_person = get_person(oid)['Person']
    existing_person.pop('_id', None)

    if 'first_name' in updates:
        existing_person['first_name'] = updates['first_name']

    if 'last_name' in updates:
        existing_person['last_name'] = updates['last_name']

    if 'assets' in updates:
        existing_person['assets'] = updates['assets']

    if 'liabilities' in updates:
        existing_person['liabilities'] = updates['liabilities']

    response = requests.patch(f'{config["connection_uri"]}/finman/person?oid={oid}', json=existing_person)
    return { 'Person': response.json() }

def delete_person(oid):
    if oid is not None:
        response = requests.delete(f'{config["connection_uri"]}/finman/person?oid={oid}')
        return response.json()
