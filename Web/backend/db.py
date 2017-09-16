import redis
import json


class DBManager():

    def __init__(self):
        self.db = redis.StrictRedis(host='localhost', port=6379, db=0)
        if not self.db.get("id_count"):
            self.db.set("id_count",0)

    def new_entry(self, data):
        self.validate_data(data,new=True)
        ip = data['ip']
        old_data = self.get_by_ip(ip)
        if old_data:
            _id = json.loads(old_data)['id']
        else:
            _id = int(self.db.get("id_count"))
            self.db.incr("id_count")
        data['id'] = _id
        key = "id=%s:%s" % (_id, ip)
        self.db.set(key,json.dumps(data))
        
    def set_by_ip(self, data):
        self.validate_data(data)
        ip = data['ip']
        key = self.db.scan(match="*%s*"%ip)[1]
        if len(key) == 1:
            self.db.set(key[0],json.dumps(data))

    def set_by_id(self,_id, data):
        self.validate_data(data, _id=_id)
        match = "id=%s*" % data['id']
        key = self.db.scan(match=match)[1]
        if len(key) == 1:
            self.db.set(key[0],json.dumps(data))
    
    def get_by_id(self, _id):
        match = "id=%s*"%str(_id)
        keys = self.db.scan(match=match)[1]
        if len(keys) == 1:
            return json.loads(self.db.get(keys[0]))

    def get_by_ip(self, ip):
        match = "*%s*" % ip
        keys = self.db.scan(match=match)[1]
        if len(keys) == 1:
            return json.loads(self.db.get(keys[0]))

    def delete_all(self):
        for k in self.db.keys():
            self.db.delete(k)
        self.db.set("id_count",0)
    
    def delete_by_ip(self,ip):
        match = "*%s*" % ip
        keys = self.db.scan(match=match)[1]
        if len(keys) == 1:
            return self.db.delete(keys[0])

    def validate_data(self, data, _id=None, new=False):
        valid = True
        required_fields = ['ip', 'type', 'state']
        for field in required_fields:
            valid = valid and (field in data)
        if not new:
            valid = valid and ('id' in data)
        if not _id==None:
            valid = valid and (data['id'] == _id)
        if not valid:
            raise Exception

    def get_all_devices(self):
        devices = []
        keys = self.db.scan(match="id=*")[1]
        keys.sort()
        for key in keys:
            devices.append(json.loads(self.db.get(key)))
        device = {}
        """
        devices = {}
        keys = self.db.scan(match="id=*")[1]
        for key in keys:
            devices[key.split(":")[0].replace("id=","")] = json.loads(self.db.get(key))
        """
        return devices

database = DBManager()
#database.delete_all()
