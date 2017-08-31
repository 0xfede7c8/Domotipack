from flask import Flask, request, abort
from flask_restful import Api, Resource
from flask_socketio import SocketIO
from db import DBManager

app = Flask(__name__)
api = Api(app)
websocket = SocketIO(app)
database = DBManager()
database.delete_all()


@app.route('/')
def index():
    return "INDEX"

class Device(Resource):
    def get(self,device_id):
        data = database.get_by_id(device_id)
        if data:
            return data, 200
        else:
            abort(404)

class DevicesList(Resource):
    def get(self):
        return database.get_all_devices()
    
    def post(self):
        json_data = request.get_json(force=True)
        try:
            database.new_entry(json_data)
            return database.get_by_ip(json_data['ip']), 201
        except:
            abort(400)

api.add_resource(DevicesList, '/api/devices')
api.add_resource(Device, '/api/devices/<device_id>')

if __name__ == '__main__':
    websocket.run(app)

