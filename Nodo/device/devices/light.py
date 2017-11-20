from ..device import Device
from time import sleep
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) ## GPIO 17 como salida
GPIO.setup(27, GPIO.OUT) ## GPIO 27 como salida

class Light(Device):

    def __init__(self, *args):
        Device.__init__(self, *args)
        self.on = 

    #when a change is made from the web
    def apply_state(self):
        pass
        #GPIO.cleanup() ## Hago una limpieza de los GPIO
        
    #monitors changes from the devices
    def monitor_changes(self):
        #self.state['state']['value'] += 10
        if self.state["state"]["on"]:
            self.strobe(self.state["state"]["value"])
        else
            GPIO.output(17, False) ## Apago el 17
        #self.devices_state.set_device(self.state, notify_server=True) 

    def strobe(width):
        factor = 1000
        GPIO.output(17, True) ## Enciendo el 17
        timeoff =  100 - width
        sleep(width / factor)
        GPIO.output(17, False) ## Apago el 17
        sleep(timeoff / factor)


