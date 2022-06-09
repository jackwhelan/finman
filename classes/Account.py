from datetime import datetime

from classes.Asset import Asset
from classes.Liability import Liability
from classes.Transaction import Transaction
from classes.Person import Person

class Account:
    def __init__(self, owner: Person, description: str, balance: float, assets: list[Asset], liabilities: list[Liability],
                 transaction_history: list[Transaction], scheduled_transactions: list[Transaction]):
        self.owner = owner
        self.description = description
        self.balance = balance
        self.assets = assets
        self.liabilities = liabilities
        self.transaction_history = transaction_history
        self.scheduled_transactions = scheduled_transactions
        self.creation_date = datetime.now()

    @property
    def assets_value(self):
        total_assets = 0
        for asset in self.assets:
            total_assets += asset.value
        return total_assets

    @property
    def liabilities_value(self):
        total_liabilities = 0
        for liability in self.liabilities:
            total_liabilities += liability.value
        return total_liabilities

    @property
    def total_value(self):
        return self.balance + self.assets_value() - self.liabilities_value()
