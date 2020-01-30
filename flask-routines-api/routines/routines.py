import json

from flask import Blueprint


bp = Blueprint('routines', __name__, url_prefix='/routines')


@bp.route('/demo', methods=('GET',))
def demo():
	return json.dumps(['Morning', 'Bedtime'])


@bp.route('/list', methods=('GET',))
def list():
	return json.dumps([])