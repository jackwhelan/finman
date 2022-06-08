from flask import Blueprint

from api.greeting import greeting_routes

api_version = Blueprint('api_version', __name__)
api_version.register_blueprint(greeting_routes, url_prefix='/v1')

@api_version.route('/v1')
def version_one():
    return 'API v1 Default Route'
