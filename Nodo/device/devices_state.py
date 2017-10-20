class DevicesState():
    def __init__(self, api):
        self.state = {}
        self.observers = []
        self.api = api
    
    def set_device(self, device_json,
                   notify_observers = False, notify_server = False):
        _id = device_json['id']
        self.state[int(_id)] = device_json
        if notify_observers:
            self.notify_observers()
        if notify_server:
            self.api.update_device(device_json)
    
    def get_state(self):
        return self.state

    def register(self, device):
        self.observers.append(device)

    def notify_observers(self):
        for observer in self.observers:
            try:
                observer.update(self.state[observer.id])
            except:
                pass
