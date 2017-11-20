import httplib
import json
import sys
import socket
import traceback
from time import sleep

from api import API, APIListener
from device.devices_state import DevicesState
from device.device import Device
from device.jsons import light_json, alarm_json
from device.devices.light import Light
from device.devices.create_device import create_device

API_URL = 'domotipack.local:5000'
SOCKET_PORT = 5001
INTERFACE = 'wlp3s0'

def get_lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8',80))
    return s.getsockname()[0]

LAN_IP = get_lan_ip()

devices_to_register = [light_json(LAN_IP), alarm_json(LAN_IP)]

def main():
    running_threads = []
    api = API(API_URL)
    devices_state = DevicesState(api)
    apiListener = APIListener(LAN_IP, SOCKET_PORT, devices_state)
    apiListener.start()
    running_threads.append(apiListener)
    try:
        #register all devices
        for device in devices_to_register:
            registered_device = api.register_device(device)
            if registered_device:
                devices_state.set_device(registered_device)
                new_device = create_device(registered_device, devices_state)
#                new_device = Light(registered_device, devices_state)
                new_device.start()
                running_threads.append(new_device)
        print devices_state.get_state()
        while True:
            sleep(1)
    except KeyboardInterrupt:
        print "interrupted"
        for t in running_threads:
            t.kill_received = True
    except:
        traceback.print_exc()
        for t in running_threads:
            t.kill_received = True
        
if __name__ == '__main__':
    main()

 
