import threading
from time import sleep

class Device(threading.Thread):
    def __init__(self, device_json, devices_state):
        threading.Thread.__init__(self)
        self.kill_received = False
        self.id = device_json['id']
        self.state = device_json
        self.devices_state = devices_state
        self.devices_state.register(self)

    def update(self, state):
        if self.state != state:
            print "observer update"
            self.state = state
            self.apply_state()

    def apply_state(self):
        print "apply_state", self.state

    def run(self):
        while not self.kill_received:
            self.monitor_changes()
        exit(0)

    def monitor_changes(self):
        sleep(1)
