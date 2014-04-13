#!/usr/bin/env python
# Traffic Lights Demo Sequence
# Runs until Ctrl/C is pressed

# Must be run as root - sudo python TrafficLights.py 

#PiDie LEDs are on physical pins as follows:
#    Led1: 7
#    Led2: 11
#    Led3: 12
#    Led4: 13
#    Led5: 15
#    Led6: 16
#    Led7: 18
#    Led8: 22
#    Led9: 8

#PiDie Buttons on physical pins as follows:
#    Red: 21
#    Green: 19
#    Yellow: 24
#    Blue: 26

import time, random, RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

LEDs = [7,8,11,12,13,15,16,18,22]

LEDOFF = 1
LEDON = 0

for pin_number in LEDs:
    GPIO.setup(pin_number, GPIO.OUT)

for pin_number in LEDs:
    GPIO.output (pin_number, LEDON)
time.sleep(5)

for pin_number in LEDs:
    GPIO.output (pin_number, LEDOFF)
time.sleep(5)

GPIO.cleanup()
