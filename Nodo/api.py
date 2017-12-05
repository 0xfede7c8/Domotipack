import httplib
import json
import socket
import threading
import traceback
from time import sleep

class API():
    def __init__(self, api_url):
       self.API_URL = api_url
    
    def register_device(self, device_json):
        connection = httplib.HTTPConnection(self.API_URL)
        connection.request("POST", "api/devices", 
                                json.dumps(device_json))
        res = connection.getresponse()
        if res.status == 201:
            response = res.read()
            print "device registered"
            return json.loads(response)

    def update_device(self, device_json):
        _id = device_json['id']
        connection = httplib.HTTPConnection(self.API_URL)
        connection.request("PUT", "/api/devices/" + str(_id),
                                json.dumps(device_json))
        res = connection.getresponse()
        #print res.status
        

class APIListener(threading.Thread):
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
                    self.devices_state.set_device(json_data,
                                                  notify_observers = True)
        except socket.timeout, e:
            pass
        except:
            traceback.print_exc()


