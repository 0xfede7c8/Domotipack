from ..device import Device

import RPi.GPIO as GPIO
from time import sleep

light_pin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(light_pin, GPIO.OUT) ## GPIO 17 como salida
led = GPIO.PWM(light_pin, 0)
led.start(0)

class Light(Device):

    def __init__(self, *args):
        Device.__init__(self, *args)

    def apply_state(self):
        if self.state["state"]["on"]:
            print "Luz encendida."
        else:
            print "Luz apagada."
        print self.state["state"]["value"]
    
    def monitor_changes(self):
        if self.state["state"]["on"]:
            self.strobe(self.state["state"]["value"])
        else:
            GPIO.output(light_pin, False)
        
    def strobe(self, width):
        """factor = 5000.0
        timeoff =  100.0 - width
        GPIO.output(light_pin, True)
        sleep(width / factor)
        GPIO.output(light_pin, False)
        sleep(timeoff / factor)
        GPIO.output(light_pin, True)
        """
        led.ChangeDutyCycle(width)

