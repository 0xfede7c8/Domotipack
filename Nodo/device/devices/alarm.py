from ..device import *
from time import sleep

import RPi.GPIO as GPIO
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.add_event_detect(23, GPIO.RISING, callback=self.alarmActivated, bouncetime=300)

class Alarm(Device):
    def __init__(self, *args):
        Device.__init__(self, *args)

    def apply_state(self):
        print self.state

    def monitor_changes(self):
        GPIO.wait_for_edge(24, GPIO.RISING)
        print "asfd"

	def alarmActivated(self, channel):  
		print "AlarmActivated" 
