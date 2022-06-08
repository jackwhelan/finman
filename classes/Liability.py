from datetime import datetime

class Liability:
    def __init__(self, name: str, description: str, value: float, last_updated: datetime):
        self.name = name
        self.description = description
        self.value = value
