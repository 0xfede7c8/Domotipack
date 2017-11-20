import httplib
import json
import sys
import socket


conn = httplib.HTTPConnection("192.168.0.64:5000")
conn.request("GET","/api/devices/0")
res = conn.getresponse()

data_str = res.read()
loaded_json = json.loads(data_str)
#loaded_json["state"]["value"] = int(sys.argv[1])

loaded_json["ip"] = "9.9.9.9"
loaded_json["type"] = "light"
loaded_json.pop("id")

print loaded_json
dumped_json = json.dumps(loaded_json)

conn.request("POST","/api/devices", dumped_json)