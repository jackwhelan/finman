from datetime import datetime

from Person import Person

class Transaction:
    def __init__(self, sender: Person, recipient: Person, amount: float):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = datetime.now()
