import device
from time import sleep
import RPi.GPIO as GPIO
import time

GPIO.setup(17, GPIO.OUT) ## GPIO 17 como salida

class Light(Device):

    def __init__(self, *args):
        Device.__init__(self, *args)

    #when a change is made from the web
    def apply_state(self):
        pass        
    #monitors changes from the devices
    def monitor_changes(self):
        #self.state['state']['value'] += 10
        if self.state["state"]["on"]:
            self.strobe(self.state["state"]["value"])
        else:
            GPIO.output(17, False) ## Apago el 17
        #self.devices_state.set_device(self.state, notify_server=True) 

    def strobe(self, width):
        factor = 5000.0
        GPIO.output(17, True) ## Enciendo el 17
        timeoff =  100.0 - width
        sleep(width / factor)
        GPIO.output(17, False) ## Apago el 17
        sleep(timeoff / factor)
        GPIO.output(17, True) ## Enciendo el 17


