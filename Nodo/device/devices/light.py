from ..device import Device

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) ## GPIO 17 como salida

class Light(Device):

    def __init__(self, *args):
        Device.__init__(self, *args)

    def apply_state(self):
        if self.state["state"]["on"]:
            print "Luz encendida."
        else:
            print "Luz apagada."
        print self.state["value"]
        pass        
    
    def monitor_changes(self):
        if self.state["state"]["on"]:
            self.strobe(self.state["state"]["value"])
        else:
            GPIO.output(17, False)
        
    def strobe(self, width):
        factor = 5000.0
        GPIO.output(17, True)
        timeoff =  100.0 - width
        sleep(width / factor)
        GPIO.output(17, False)
        sleep(timeoff / factor)
        GPIO.output(17, True)


