from flask import Flask, request, abort, render_template
from db import DBManager
from api import api_bp, websocket
from flask_cors import CORS
from flask import Blueprint
import socket

app = Flask(__name__, template_folder='public')
app.register_blueprint(api_bp, url_prefix='/api')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
@app.route('/')
def index():
    return render_template('index.html', ip=get_ip())

if __name__ == '__main__':
    websocket.init_app(app)
    websocket.run(app, host="0.0.0.0", debug=True)
