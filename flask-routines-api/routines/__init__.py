from flask import Flask, request
import json

from .routines import bp

__version__ = '0.0.1'


app = Flask(__name__, instance_relative_config=True)
config_path = 'config/' + app.config['ENV'] + '.py'
app.config.from_pyfile(config_path, silent=True)

app.register_blueprint(bp)


@app.route('/version')
def version():
    return json.dumps({'version': __version__})


@app.route('/')
def index():
    return json.dumps({
        'urls': [
            request.base_url + 'version',
            request.base_url + 'routines',
        ]
    })
