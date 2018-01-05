
'''
Ultrasonic socket.
Returns distance measured.
Average return times of 0.02 seconds.
'''

# Import required Python libraries
from __future__ import print_function
import time
import RPi.GPIO as GPIO

def measure():
    # Use BCM GPIO references
    # instead of physical pin numbers
    GPIO.setmode(GPIO.BCM)

    # Define GPIO to use on Pi
    GPIO_TRIGGER = 24
    GPIO_ECHO    = 23

    # Speed of sound in cm/s at temperature
    temperature = 32
    speedSound = 33100 + (0.6*temperature)

    print("Ultrasonic Measurement")
    print("Speed of sound is",speedSound/100,"m/s at ",temperature,"deg")

    # Set pins as output and input
    GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
    GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

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

if __name__=='__main__':
    measure()
