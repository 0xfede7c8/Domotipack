def light_json(ip, default_value = 0):
    return {"ip": ip, 
            "state": {"on": True, "value": default_value},
            "type": "light"}

def alarm_json(ip):
    return {"ip": ip,
            "state": {"active": False, "armed": True}, 
            "type":"alarm"}
