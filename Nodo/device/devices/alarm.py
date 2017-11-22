from ..device import Device
from time import sleep

import RPi.GPIO as GPIO

alarm_pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(alarm_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


class Alarm(Device):
    def __init__(self, *args):
        Device.__init__(self, *args)
        GPIO.add_event_detect(alarm_pin, GPIO.RISING, callback=self.alarmActivated, bouncetime=300)

    def apply_state(self):
        print self.state

    def monitor_changes(self):
        sleep(1)

    def alarmActivated(self, channel):
        print "Sensor Activado."
        if self.state["state"]["armed"]:
        	self.state["state"]["active"] = True
        	self.devices_state.set_device(self.state, notify_server=True) 
        	print "Notifico al concentrador."
