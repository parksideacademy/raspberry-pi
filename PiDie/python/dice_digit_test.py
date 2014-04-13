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
NUMBER1 = [13]              #Led 4
NUMBER2 = [7,18]            #Led 1 and 7
NUMBER3 = [7,13,18]         #Led 1, 4 and 7
NUMBER4 = [7,12,15,18]      #Led 1, 3, 5 and 7
NUMBER5 = [7,12,13,15,18]   #Led 1, 3, 4, 5 and 7
NUMBER6 = [7,8,12,15,18,22] #Led 1, 3, 5, 7, 8 and 9

LEDOFF = 1
LEDON = 0

for pin_number in LEDs:
    GPIO.setup(pin_number, GPIO.OUT)

#Show 1 on the Dice
for pin_number in NUMBER1:
    GPIO.output (pin_number, LEDON)
time.sleep(2)
for pin_number in LEDs:
    GPIO.output (pin_number, LEDOFF)

#Show 2 on the Dice
for pin_number in NUMBER2:
    GPIO.output (pin_number, LEDON)
time.sleep(2)
for pin_number in LEDs:
    GPIO.output (pin_number, LEDOFF)
    
#Show 3 on the Dice
for pin_number in NUMBER3:
    GPIO.output (pin_number, LEDON)
time.sleep(2)
for pin_number in LEDs:
    GPIO.output (pin_number, LEDOFF)

#Show 4 on the Dice
for pin_number in NUMBER4:
    GPIO.output (pin_number, LEDON)
time.sleep(2)
for pin_number in LEDs:
    GPIO.output (pin_number, LEDOFF)

#Show 5 on the Dice
for pin_number in NUMBER5:
    GPIO.output (pin_number, LEDON)
time.sleep(2)
for pin_number in LEDs:
    GPIO.output (pin_number, LEDOFF)

#Show 6 on the Dice
for pin_number in NUMBER6:
    GPIO.output (pin_number, LEDON)
time.sleep(2)
for pin_number in LEDs:
    GPIO.output (pin_number, LEDOFF)
    
GPIO.cleanup()
