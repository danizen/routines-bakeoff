import json

from flask import Blueprint, request
from pynamodb.exceptions import PynamoDBException

from .utils import PynamoEncoder
from .models import Routine


bp = Blueprint('routines', __name__, url_prefix='/routines')


@bp.route('/', methods=('GET',))
def index():
    return json.dumps({
        'urls': [
            request.base_url + 'of',
        ]
    })


@bp.route('/of', methods=('GET',))
def users():
    encoder = PynamoEncoder()
    try:
        results = dict(
            (r.user, request.base_url + '/' + r.user)
            for r in Routine.scan(attributes_to_get=['user'])
        )
        return encoder.encode({'results': results})
    except PynamoDBException as e:
        return encoder.encode({
            'error': {
                'code': e.cause_response_code,
                'message': e.cause_reponse_message
            }
        })


@bp.route('/of/<username>', methods=('GET',))
def list(username):
    encoder = PynamoEncoder()
    try:
        results = [r for r in Routine.query(username)]
        return encoder.encode({'results': results})
    except PynamoDBException as e:
        return encoder.encode({
            'error': {
                'code': e.cause_response_code,
                'message': e.cause_reponse_message
            }
        })


@bp.route('/of/<username>/<routine>', methods=('GET',))
def detail(username, routine):
    encoder = PynamoEncoder()
    try:
        results = Routine.get(username, routine)
        return encoder.encode({'results': results})
    except Routine.DoesNotExist as e:
        return encoder.encode({
            'error': {
                'code': 'DoesNotEist',
                'message': str(e)
            }
        })
    except PynamoDBException as e:
        return encoder.encode({
            'error': {
                'code': e.cause_response_code,
                'message': e.cause_reponse_message
            }
        })
