from db import DBManager
import pdb

red = DBManager()

new_device = '{ "ip": "192.168.0.50" , "type":"light" , "state" : { "on" :\
"on", "brightness": "100%" } } '

device_update =  '{"id":1, "ip": "192.168.0.50" , "type":"light" , "state" : { "on" :\
"on", "brightness": "80%" } } '

red.new_entry(new_device)
print red.get_by_id(0)
