from flask import Flask, request, abort, render_template
from db import DBManager
from api import api_bp, websocket
from flask_cors import CORS
from flask import Blueprint

app = Flask(__name__, template_folder='public')
app.register_blueprint(api_bp, url_prefix='/api')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    websocket.init_app(app)
    websocket.run(app, host="0.0.0.0", debug=True)
