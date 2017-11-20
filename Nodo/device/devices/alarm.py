from ..device import Device
from time import sleep

class Alarm(Device):
    def __init__(self, *args):
        Device.__init__(self, *args)

    def apply_state(self):
        print "overwritten apply_state", self.state

    def monitor_changes(self):
        pass
