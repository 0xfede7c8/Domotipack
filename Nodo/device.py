import httplib
import json
import sys
import socket
import threading
import netifaces
import traceback
from time import sleep

API_URL = '192.168.1.12:5000'
SOCKET_PORT = 5001
INTERFACE = 'wlp3s0'

lan_ip = netifaces.ifaddresses(INTERFACE)[netifaces.AF_INET][0]['addr']

light_json = {"ip": lan_ip, "state": {"on": True, "value": 100}, "type": "light"}
alarm_json = {"ip": lan_ip, "state": "active", "type":"alarm"}
devices_to_register = [light_json , alarm_json]

class devicesState():
    def __init__(self):
        self.state = {}
    
    def set_device(self, device_json):
        print device_json
        id = device_json['id']
        self.state[int(id)] = device_json
    
    def get_state(self):
        return self.state

def register_device(device_json, devices_state):
    connection = httplib.HTTPConnection(API_URL)
    connection.request("POST","/api/devices", json.dumps(device_json))
    res = connection.getresponse()
    if res.status == 201:
        response = res.read()
        response_json = json.loads(response)
        devices_state.set_device(response_json)
        print "device registered"

def update_device(device_json):
    connection = httplib.HTTPConnection(API_URL)
    id = device_json['id']
    connection.request("PUT","/api/devices/" + str(id), json.dumps(device_json))

def changeState(value):
	light_json["state"]["value"] = value
	light_json_str = json.dumps(light_json)
	conn = httplib.HTTPConnection("192.168.0.64:5000")
	conn.request("PUT","/api/devices/" + str(id), light_json_str)	

class SocketThread(threading.Thread):
    def __init__(self, host_ip, port, devices_state):
        threading.Thread.__init__(self)
        self.kill_received = False
        self.devices_state = devices_state
        self.socket_api = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_api.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket_api.bind((host_ip,port))
        self.socket_api.settimeout(0.1)
        self.socket_api.listen(1)

    def run(self):
        while not self.kill_received:
            self.receive()
        self.socket_api.close()
        exit(0)

    def receive(self):
        size = 1024
        try:
            client, address = self.socket_api.accept()
            data = client.recv(size)
            if data:
                json_data = json.loads(data)
                if json_data['type'] == 'keepalive':
                    if json_data['id'] in self.devices_state.state:
                        client.send("ALIVE")
                    else:
                        client.send("DEAD")
                else:
                    self.devices_state.set_device(json_data)
                    print "update from server, new state:"
                    print self.devices_state.get_state()
        except socket.timeout, e:
            pass
        except:
            traceback.print_exc()

def main():
    devices_state = devicesState()
    socketThread = SocketThread(lan_ip, SOCKET_PORT, devices_state)
    socketThread.start()
    try:
        #register all devices
        for device in devices_to_register:
            register_device(device, devices_state)
        print devices_state.get_state()
        while True:
            sleep(5)
            print devices_state.get_state()
    except KeyboardInterrupt:
        print "interrupted"
        socketThread.kill_received = True
    except:
        traceback.print_exc()
        socketThread.kill_received = True
        
if __name__ == '__main__':
    main()

 
