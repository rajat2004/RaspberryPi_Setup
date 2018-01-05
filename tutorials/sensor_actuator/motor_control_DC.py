'''
Configure timed pulse based motion movement

Subject to reliability of the Linux clock

'''

import sys
import time
import RPi.GPIO as GPIO
import math

mode=GPIO.getmode()
print mode
GPIO.cleanup()

sleeptime=1

## CONSTANTS
Forward=17
Backward=27
PWM_PIN=22
RPM=100.00
RPM_C=(DISC_RPM/60)*2*math.pi

## SETUP
GPIO.setmode(GPIO.BCM)

GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)
GPIO.setup(PWM_PIN,GPIO.OUT)

PWM = GPIO.PWM(PWM_PIN,100)
PWM.start(85)

def forward(theta):

    t=theta/DISC_RPM_C

    GPIO.output(Forward, GPIO.HIGH)
    GPIO.output(Backward, GPIO.LOW)

    print("Moving Forward by theta \t",theta)
    time.sleep(t)
    GPIO.output(Forward, GPIO.LOW)

def reverse(theta):
    t=theta/DISC_RPM_C

    GPIO.output(Forward, GPIO.LOW)
    GPIO.output(Backward, GPIO.HIGH)

    print("Moving Backward by theta \t",theta)
    time.sleep(t)
    GPIO.output(DISC_Backward, GPIO.LOW)


#####
# Time based implementations
####

def forward_time(t):

    GPIO.output(Forward, GPIO.HIGH)
    GPIO.output(Backward, GPIO.LOW)

    print("Moving Forward for time \t", t)
    time.sleep(t)
    GPIO.output(Forward, GPIO.LOW)


def reverse_time(t):

    GPIO.output(Backward, GPIO.HIGH)
    GPIO.output(Forward, GPIO.LOW)

    print("Moving Backward for time \t", t)
    time.sleep(t)
    GPIO.output(Backward, GPIO.LOW)

    #GPIO.cleanup()

if __name__=='__main__':

    while (1):
        #DISC_and_BRUSH_forward_angle(180)
        #DISC_reverse_time(0.685)
        reverse_time(0.2)
        #BRUSH_forward_time(0.165)
        #BRUSH_forward_time(0.5)
        time.sleep(1)
        #DISC_reverse(6*math.pi)

        #BRUSH_forward(math.pi)
        #BRUSH_reverse(math.pi)

    GPIO.cleanup()
