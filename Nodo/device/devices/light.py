from ..device import Device
from time import sleep

class Light(Device):

    def __init__(self, *args):
        Device.__init__(self, *args)

    #when a change is made from the web
    def apply_state(self):
        print "overwritten apply_state", self.state

    #monitors changes from the devices
    def monitor_changes(self):
        for i in range(10):
            if not self.kill_received:
                sleep(2)
                self.state['state']['value'] += 10
                self.devices_state.set_device(self.state, notify_server=True)
        self.kill_received = True
