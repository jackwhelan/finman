from datetime import datetime
from bson.objectid import ObjectId

from etc.exceptions import CreateAssetException

class Asset:
    def __init__(self, name: str, description: str, value: float, last_updated: datetime, oid=None):
        if not oid:
            oid = ObjectId()
        elif not ObjectId.is_valid(oid):
            raise CreateAssetException(f'Object ID "{oid}" is not valid.')

        if not name.isalpha():
            raise CreateAssetException('Asset name must only contain letters.')

        if not (len(name) > 1 and len(name)) <= 30:
            raise CreateAssetException('Asset name must be between 2 and 30 characters in length.')

        if not description.isalpha():
            raise CreateAssetException('Asset description must only contain letters.')

        if not (len(description) > 1 and len(description) <= 30):
            raise CreateAssetException('Asset description must be between 2 and 30 characters in length.')

        if value < 0:
            value *= -1

        self.name = name
        self.description = description
        self.value = value
        self.last_updated = last_updated
        self.oid = oid
