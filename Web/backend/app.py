from flask import Flask, request, abort
from db import DBManager
from api import api_bp, websocket
from flask_cors import CORS
from flask import Blueprint

#api_bp = Blueprint('api', 'api')
app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/api')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def index():
    return "INDEX"

if __name__ == '__main__':
    websocket.init_app(app)
    websocket.run(app, host="0.0.0.0")

