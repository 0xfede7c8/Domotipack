import redis
import json


class DBManager():

    def __init__(self):
        self.db = redis.StrictRedis(host='localhost', port=6379, db=0)
        self.db.set("id_count",0)

    def new_entry(self, data):
        self.validate_data(data,new=True)
        ip = data['ip']
        _id = int(self.db.get("id_count"))
        self.db.incr("id_count")
        data['id'] = _id
        key = "id=%s:%s" % (_id, ip)
        self.db.set(key,data)
        
    def set_by_ip(self, data):
        validate_data(data)
        ip = data['ip']
        key = self.db.scan(match="*%s*"%ip)[1]
        if len(key) == 1:
            self.db.set(key[0],data)

    def set_by_id(self, data):
        validate_data(data)
        match = "id=%s*" % data['id']
        key = self.db.scan(match=match)[1]
        if len(key) == 1:
            self.db.set(key[0],data)
    
    def get_by_id(self, _id):
        match = "id=%s*"%str(_id)
        keys = self.db.scan(match=match)[1]
        if len(keys) == 1:
            return self.db.get(keys[0])

    def get_by_ip(self, ip):
        match = "*%s*" % ip
        keys = self.db.scan(match=match)[1]
        if len(keys) == 1:
            return self.db.get(keys[0])

    def delete_all(self):
        for k in self.db.keys():
            self.db.delete(k)
        self.db.set("id_count",0)
    
    def delete_by_ip(self,ip):
        match = "*%s*" % ip
        keys = self.db.scan(match=match)[1]
        if len(keys) == 1:
            return self.db.delete(keys[0])

    def validate_data(self, data, new=False):
        valid = True
        required_fields = ['ip', 'type']
        for field in required_fields:
            valid = valid and (field in data)
        if not new:
            valid = valid and ('id' in data)
        if not valid:
            raise Exception

    def get_all_devices(self):
        devices = {}
        keys = self.db.scan(match="id=*")[1]
        for key in keys:
            devices[key.split(":")[0].replace("id=","")] = self.db.get(key)
        return devices
