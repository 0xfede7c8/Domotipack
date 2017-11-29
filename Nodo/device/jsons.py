def light_json(ip, default_value = 0):
    return {"ip": ip, 
            "state": {"on": False, "value": default_value},
            "type": "light"}

def alarm_json(ip):
    return {"ip": ip,
            "state": {"active": False, "armed": False}, 
            "type":"alarm"}

def dht11_json(ip):
    return {"ip": ip,
            "state": {},
            "type": "dht11"
