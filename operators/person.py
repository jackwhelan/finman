import requests

from classes.Person import Person
from exceptions import CreatePersonException

def create_person(first_name: str, last_name: str):
    Person(first_name, last_name)

    payload = {
        "first_name": first_name,
        "last_name": last_name
    }

    # TODO: Replace occurences of data-access api with config var
    response = requests.post(f'http://data-access:5000/finman/person', json=payload)
    return response.json()

def get_person(oid):
    # TODO: Refactor
    if oid is not None:
        response = requests.get(f'http://data-access:5000/finman/person?oid={oid}')
        return { 'Person': response.json()['response'] }
    people = []
    response = requests.get(f'http://data-access:5000/finman/person')
    for person in response.json()['response']:
        people.append(Person(person['first_name'], person['last_name'], person['_id']).__dict__)
    return { 'People': people }

def update_person(oid, updates: dict):
    if not oid:
        raise CreatePersonException('Could not update Person without object ID. Please pass a valid Person oid as a url argument')

    # The reason for creating a new payload instead of directly using the updates dictionary is to enforce only modifying
    # existing Person fields rather than allowing the API to add non existing values using a patch request.
    payload = {}

    if 'first_name' in updates:
        payload['first_name'] = updates['first_name']

    if 'last_name' in updates:
        payload['last_name'] = updates['last_name']

    response = requests.patch(f'http://data-access:5000/finman/person?oid={oid}', json=payload)
    return { 'Person': response.json() }

def delete_person(oid):
    if oid is not None:
        response = requests.delete(f'http://data-access:5000/finman/person?oid={oid}')
        return response.json()
