'''
Ultrasonic and Motor socket for Flask.
Returns distance measured.
Average return times of 0.02 seconds.
'''
# Import required Python libraries
from __future__ import print_function
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO    = 24

# Speed of sound in cm/s at temperature
temperature = 32
speedSound = 33100 + (0.6*temperature)

class Raspi(object):

    def __init__(self):
        pass

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_TRIGGER, GPIO.IN)
        GPIO.setup(GPIO_ECHO, GPIO.OUT)


    def read_sensor(self):
        print("Ultrasonic Measurement")
        print("Speed of sound is",speedSound/100,"m/s at ",temperature,"deg")

        # Set trigger to False (Low)
        GPIO.output(GPIO_TRIGGER, False)

        # Allow module to settle
        time.sleep(0.5)

        # Send 10us pulse to trigger
        GPIO.output(GPIO_TRIGGER, True)
        # Wait 10us
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)


        while GPIO.input(GPIO_ECHO)==0:
          pass

        start = time.time()

        while GPIO.input(GPIO_ECHO)==1:
          pass
        stop = time.time()
        # Calculate pulse length
        elapsed = stop-start

        # Distance pulse travelled in that time is time
        # multiplied by the speed of sound (cm/s)
        distance = elapsed * speedSound

        # That was the distance there and back so halve the value
        distance = distance / 2

        print("Distance : {0:5.1f}".format(distance))

        # Reset GPIO settings
        GPIO.cleanup()

        return distance
        return GPIO.input(SENSOR_PIN)
    '''

    def change_led(self, value):
        GPIO.output(LED_PIN, value)
    '''
