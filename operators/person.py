import logging
import requests

from classes.Person import Person

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
    if oid is not None:
        response = requests.get(f'http://data-access:5000/finman/person?oid={oid}')
        return { 'Person': response.json() }
    people = []
    response = requests.get(f'http://data-access:5000/finman/person')
    for person in response.json():
        logging.error(person)
        people.append(Person(person['first_name'], person['last_name'], person['_id']['$oid']).__dict__)
    return { 'People': people }

def update_person():
    pass

def delete_person():
    pass
