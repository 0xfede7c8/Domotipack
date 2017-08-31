from flask import request, abort, Blueprint
from flask_restful import Api, Resource
from db import database


api_bp = Blueprint('api', __name__)
api = Api(api_bp)


class Device(Resource):
    def get(self,device_id):
        data = database.get_by_id(device_id)
        if data:
            return data, 200
        else:
            abort(404)
    def put(self,device_id):
        json_data = request.get_json(force=True)
        try:
            database.set_by_id(data=json_data,_id = int(device_id))
            return database.get_by_id(json_data['id']), 200
        except:
            abort(400)


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


api.add_resource(DevicesList, '/devices')
api.add_resource(Device, '/devices/<device_id>')

