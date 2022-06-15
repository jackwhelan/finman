from flask import Flask

from api.api_version import api_version
from classes.Account import Account
from classes.Liability import Liability
from classes.Person import Person
from classes.Asset import Asset
from etc.logger import initialize_logging

initialize_logging()

app = Flask(__name__)
app.register_blueprint(api_version)

@app.route('/')
def default_route():
    return 'Default Route, Please Specify API Version.'

def seed_data():
    jack = Person("Jack", "Whelan")
    jacks_assets = [
        Asset("Midleton Very Rare 2021", "Bottle of rare whiskey.", 264.5, '05/06/2022'),
        Asset("Midleton Very Rare 2020", "Bottle of rare whiskey.", 705.7, '05/06/2022'),
        Asset("Midleton Very Rare 2019", "Bottle of rare whiskey.", 401.67, '05/06/2022'),
        Asset("Midleton Very Rare 2018", "Bottle of rare whiskey.", 392.5, '05/06/2022'),
        Asset("Midleton Very Rare 2017", "Bottle of rare whiskey.", 697.27, '05/06/2022'),
        Asset("Midleton Very Rare 2016", "Bottle of rare whiskey.", 433.75, '05/06/2022'),
        Asset("Midleton Very Rare Single Cask 2001", "Bottle of rare whiskey.", 700, '05/06/2022')
    ]
    jacks_liabilities = [
        Liability("Bens Wedding Gift", "Still owe ben €150/€500 for his wedding gift.", 150, '05/06/2022')
    ]
    return Account(jack, "Worth", 20000, jacks_assets, jacks_liabilities, None, None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=False)
