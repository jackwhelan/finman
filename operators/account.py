from classes.Transaction import Transaction
from classes.Liability import Liability
from classes.Account import Account
from classes.Person import Person
from classes.Asset import Asset

import requests
from bson.objectid import ObjectId

from exceptions import AccountOperatorException

def create_account(owner: Person, description: str, balance: float, assets: list[Asset], liabilities: list[Liability],
                 transaction_history: list[Transaction], scheduled_transactions: list[Transaction]):
    return Account(owner, description, balance, assets, liabilities, transaction_history, scheduled_transactions)

def get_account(oid: ObjectId):
    response = requests.get(f'http://data-access/finman/account', {'oid': oid})
    retrieved_account = Account(response['owner'], response['description'], response['balance'], response['assets'],
                                response['liabilities'], response['transaction_history'], response['scheduled_transactions'])
    return retrieved_account

def update_account():
    pass

def delete_account():
    pass
