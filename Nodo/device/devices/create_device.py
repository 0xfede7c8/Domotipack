from light import Light
from alarm import Alarm
from thsensor import THSensor

def create_device(device_json, *args):
    options = {
        'light': Light,
        'alarm': Alarm,
        'thsensor': THSensor
    }
    try:
        print device_json
        return options[device_json['type']](device_json, *args)
    except:
        return None
