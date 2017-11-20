from ..device import Device
from time import sleep

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

class Alarm(Device):
    def __init__(self, *args):
        Device.__init__(self, *args)
        try:
        	GPIO.add_event_detect(23, GPIO.RISING, callback=self.alarmActivated, bouncetime=300)
        except:
        	print "caca"
    def apply_state(self):
        print self.state

    def monitor_changes(self):
        sleep(1)

	def alarmActivated(self, channel):  
		print "AlarmActivated" 
