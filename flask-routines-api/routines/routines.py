import json

from flask import Blueprint


bp = Blueprint('routines', __name__, url_prefix='/routines')


@bp.route('/list', methods=('GET',))
def list():
	return json.dumps(['Morning', 'Bedtime'])
