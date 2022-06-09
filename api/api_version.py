from flask import Blueprint

from api.account import account_routes
from api.person import person_routes

api_version = Blueprint('api_version', __name__)
api_version.register_blueprint(account_routes, name='account_routes', url_prefix='/v1')
api_version.register_blueprint(person_routes, name='person_routes', url_prefix='/v1')

@api_version.route('/v1')
def version_one():
    return {
        'API v1 Default Route':
            {
                'account_routes': '/account',
                'person_routes': '/person'
            }
        }
