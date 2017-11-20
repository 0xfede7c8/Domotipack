from flask import request, abort, Blueprint
from flask_restful import Api, Resource
from db import database
from flask_socketio import SocketIO
from apscheduler.schedulers.background import BackgroundScheduler
import socket
import traceback
import json

SOCKET_PORT = 5001

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

websocket = SocketIO()

beat_scheduler = BackgroundScheduler()
beat_scheduler.start()

def keepalive_beat():
    devices = database.get_all_devices()
    size = 1024
    for device in devices:
        try:
            device_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            device_socket.settimeout(0.5)
            device_socket.connect((device['ip'],SOCKET_PORT))
            keepalive_json = {'type': 'keepalive', 'id': device['id']}
            device_socket.send(json.dumps(keepalive_json))
            response = device_socket.recv(size)
            if response == "DEAD":
                database.delete_by_id(device['id'])
        except:
            database.delete_by_id(device['id'])
            print "fallo la coneccion del socket"
    websocket.emit('update_devices', database.get_all_devices(),
                    broadcast=True)

beat_scheduler.add_job(keepalive_beat, 'interval', seconds=3)

class Device(Resource):
    def get(self,device_id):
        data = database.get_by_id(device_id)
        if data:
            return data, 200
        else:
            abort(404)

    def put(self,device_id):
        json_data = request.get_json(force=True)
        old_device = database.get_by_id(int(device_id))
        try:
            database.set_by_id(data=json_data,_id = int(device_id))
            device_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            device_socket.settimeout(0.5)
            device_socket.connect((json_data['ip'],SOCKET_PORT))
            device_socket.send(json.dumps(json_data))
            websocket.emit('update_devices', database.get_all_devices(), 
                            broadcast=True)
            return database.get_all_devices()
        except:
            database.set_by_id(data=old_device,_id = int(device_id))
            return database.get_all_devices()


class DevicesList(Resource):
    def get(self):
        return database.get_all_devices()
    
    def post(self):
        json_data = request.get_json(force=True)
        try:
            _id = database.new_entry(json_data)
            websocket.emit('update_devices', database.get_all_devices(), 
                            broadcast=True)
            return database.get_by_id(_id), 201
        except:
            abort(400)


api.add_resource(DevicesList, '/devices')
api.add_resource(Device, '/devices/<device_id>')

