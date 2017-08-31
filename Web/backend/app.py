from flask import Flask, request, abort
from flask_socketio import SocketIO
from db import DBManager
from api import api_bp


app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/api')
websocket = SocketIO(app)


@app.route('/')
def index():
    return "INDEX"

if __name__ == '__main__':
    websocket.run(app)

