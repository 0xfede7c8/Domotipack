import httplib
import json
import sys
import socket
import threading
from time import sleep


light_json = {"ip": "192.168.0.6", "state": {"on": True, "value": 100}, "type": "light"}
light_json_str = json.dumps(light_json)

#registro dispositivo
conn = httplib.HTTPConnection("192.168.0.64:5000")
conn.request("POST","/api/devices", light_json_str)
res = conn.getresponse()
light_json = json.loads(res.read())
id = light_json["id"]


host = "192.168.0.6"
port = 5001
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)

def changeState(value):
	light_json["state"]["value"] = value
	light_json_str = json.dumps(light_json)
	conn = httplib.HTTPConnection("192.168.0.64:5000")
	conn.request("PUT","/api/devices/" + str(id), light_json_str)	




value = 0 
def receive():
	while(True):
		client, address = s.accept()
		data = client.recv(size)
		if data:  
			light_json = json.loads(data)
			value = light_json["state"]["value"]
			print light_json

t2 = threading.Thread(target = receive)
t2.start()

while(True):
	t = threading.Thread(target=changeState, args=(value,))
	value += 5
	if value > 100:
		value = 0
	t.start()
	sleep(5)


    	   