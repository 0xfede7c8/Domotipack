from ..device import Device
from time import sleep

import RPi.GPIO as GPIO

alarm_pin = 23
switch_pin = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(alarm_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


class Alarm(Device):
    def __init__(self, *args):
        Device.__init__(self, *args)
        GPIO.add_event_detect(alarm_pin, GPIO.RISING, callback=self.alarm_activated, bouncetime=300)
        GPIO.add_event_detect(switch_pin, GPIO.RISING, callback=self.switch_alarm, bouncetime=300)

    def apply_state(self):
        if not self.state["state"]["armed"]:
            self.state["state"]["active"] = False
            self.devices_state.set_device(self.state, notify_server=True)
            print "Alarma desactivado"

    def monitor_changes(self):
        sleep(1)

    def alarm_activated(self, channel):
        print "Movimiento detectado"
        if self.state["state"]["armed"]:
        	self.state["state"]["active"] = True
        	self.devices_state.set_device(self.state, notify_server=True) 
        	print "Alarma activada"

    def switch_alarm(self, channel):
        print "switch alarm"
        self.state["state"]["armed"] = not self.state["state"]["armed"]
        self.state["state"]["active"] = False
        self.devices_state.set_device(self.state, notify_server=True) 

