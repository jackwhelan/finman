from datetime import datetime

class Asset:
    def __init__(self, name: str, description: str, value: float, last_updated: datetime):
        self.name = name
        self.description = description
        self.value = value
        self.last_updated = last_updated
