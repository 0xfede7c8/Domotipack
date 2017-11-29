from light import Light
from alarm import Alarm

def create_device(device_json, *args):
    options = {
        'light': Light,
        'alarm': Alarm,
        'dht11': Dht11
    }
    try:
        return options[device_json['type']](device_json, *args)
    except:
        return None
