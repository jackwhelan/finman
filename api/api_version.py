from flask import Blueprint

from api.person import person_routes
from api.liability import liability_routes

api_version = Blueprint('api_version', __name__)
api_version.register_blueprint(person_routes, name='person_routes', url_prefix='/v1')
api_version.register_blueprint(liability_routes, name='liability_routes', url_prefix='/v1')

@api_version.route('/v1')
def version_one():
    return {
        'API v1 Default Route':
            {
                'person_routes': '/person',
                'liability_routes': '/liability'
            }
        }
