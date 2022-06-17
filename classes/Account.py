from datetime import datetime

from classes.Asset import Asset
from classes.Liability import Liability
from classes.Transaction import Transaction
from classes.Person import Person

class Account:
    def __init__(self, owner: Person, description: str, balance: float, transaction_history: list[Transaction],
                 scheduled_transactions: list[Transaction]):
        self.owner_id = owner
        self.description = description
        self.balance = balance
        self.transaction_history = transaction_history
        self.scheduled_transactions = scheduled_transactions
        self.creation_date = datetime.now()
