from ..device import Device

import RPi.GPIO as GPIO
from time import sleep

from math import pow

light_pin = 24
brightup_pin = 14
brightdown_pin = 15
switch_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(light_pin, GPIO.OUT)
GPIO.setup(brightup_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(brightdown_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

class Light(Device):

    def __init__(self, *args):
        Device.__init__(self, *args)
        GPIO.add_event_detect(brightup_pin, GPIO.RISING, callback=self.bright_up, bouncetime=250)
        GPIO.add_event_detect(brightdown_pin, GPIO.RISING, callback=self.bright_down, bouncetime=250)
        GPIO.add_event_detect(switch_pin, GPIO.RISING, callback=self.switch_light, bouncetime=500)

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
        width = pow(100.0, width/100.0) - 1
        factor = 5000.0
        timeoff =  100.0 - width
        GPIO.output(light_pin, True)
        sleep(width / factor)
        GPIO.output(light_pin, False)
        sleep(timeoff / factor)
        GPIO.output(light_pin, True)
    
    def bright_up(self, channel):
        print "bright up"
        if not self.state["state"]["on"]:
            self.state["state"]["on"] = True
        self.state["state"]["value"] = self.state["state"]["value"] + 10
        if self.state["state"]["value"] > 100:
            self.state["state"]["value"] = 100
        self.devices_state.set_device(self.state, notify_server=True) 

    def bright_down(self, channel):
        print "bright down"
        self.state["state"]["value"] = self.state["state"]["value"] - 10
        if self.state["state"]["value"] <= 0:
            self.state["state"]["value"] = 0
            self.state["state"]["on"] = False
        self.devices_state.set_device(self.state, notify_server=True) 
    
    def switch_light(self, channel):
        print "switch light"
        if self.state["state"]["on"]:
            self.state["state"]["on"] = False
            self.state["state"]["value"] = 0
        else:
            self.state["state"]["on"] = True
            self.state["state"]["value"] = 100
        self.devices_state.set_device(self.state, notify_server=True) 
            
