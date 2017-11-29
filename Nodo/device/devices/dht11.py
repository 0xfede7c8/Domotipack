from ..device import Device
from time import sleep
import json
from dht11 import get_dht11

class Dht11(Device):
    def __init__(self, *args):
        Device.__init__(self, *args)

    def apply_state(self):
        pass

    def monitor_changes(self):
        self.state["state"] = json.loads.get_dht11()
        self.devices_state.set_device(self.state, notify_server=True)
        sleep(2)
