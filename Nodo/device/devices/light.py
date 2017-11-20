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

    #when a change is made from the web
    def apply_state(self):
        print self.state
         print "Ejecucion iniciada..."
        iteracion = 0
        while iteracion < 1: ## Segundos que durara la funcion
                GPIO.output(17, True) ## Enciendo el 17
                GPIO.output(27, False) ## Apago el 27
                time.sleep(1) ## Esperamos 1 segundo
                GPIO.output(17, False) ## Apago el 17
                GPIO.output(27, True) ## Enciendo el 27
                time.sleep(1) ## Esperamos 1 segundo
                iteracion = iteracion + 2 ## Sumo 2 porque he hecho dos parpadeos
        print "Ejecucion finalizada"
        GPIO.cleanup() ## Hago una limpieza de los GPIO

    #monitors changes from the devices
    def monitor_changes(self):
        for i in range(10):
            if not self.kill_received:
                sleep(2)
                self.state['state']['value'] += 10
                self.devices_state.set_device(self.state, notify_server=True)
        self.kill_received = True
