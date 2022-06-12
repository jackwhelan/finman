from bson.objectid import ObjectId
from exceptions import CreatePersonException

class Person:
    def __init__(self, first_name: str, last_name: str, oid=None):
        if not oid:
            oid = ObjectId()
        elif not ObjectId.is_valid(oid):
            raise CreatePersonException(f'Object ID "{oid}" is not valid.')

        if not first_name.isalpha():
            raise CreatePersonException('First name must only contain letters.')

        if not last_name.isalpha():
            raise CreatePersonException('Last name must only contain letters.')

        if not len(first_name) > 1 and len(first_name <= 30):
            raise CreatePersonException('First name must be between 2 and 30 characters in length.')

        if not len(last_name) > 1 and len(last_name <= 30):
            raise CreatePersonException('Last name must be between 2 and 30 characters in length.')

        self.first_name = first_name
        self.last_name = last_name
        self.oid = oid

    def __str__(self):
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'
