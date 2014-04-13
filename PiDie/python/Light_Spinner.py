# Light Spinner

# Must be run as root - sudo python Light_Spinner.py 

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

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)

#Set up the LEDs as outputs on GPIO
LEDs = [7,8,11,12,13,15,16,18,22]
for pin_number in LEDs:
    GPIO.setup(pin_number, GPIO.OUT)
    
LEDOFF = 1
LEDON = 0

#Set up the LEDs as inputs on GPIO
SWITCHs = [19,21,24,26]
for pin_number in SWITCHs:
    GPIO.setup(pin_number,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GREEN_BUTTON = 19
RED_BUTTON = 21
YELLOW_BUTTON = 24
BLUE_BUTTON = 26

#Test all LEDs    
def ALL_ON():
    for pin_number in LEDs:
        GPIO.output (pin_number, LEDON)    

def ALL_OFF():
    for pin_number in LEDs:
        GPIO.output (pin_number, LEDOFF)
ALL_OFF()

POSTION1 = [22,8,13]
POSTION2 = [15,12,13]
POSTION3 = [16,11,13]
POSTION4 = [18,7,13]

SPEED = 0.85

for i in range(5):
    for pin_number in POSTION1:
        GPIO.output (pin_number, LEDON)      
    time.sleep(SPEED)
    ALL_OFF()
    for pin_number in POSTION2:
        GPIO.output (pin_number, LEDON)      
    time.sleep(SPEED)
    SPEED -= 0.05
    ALL_OFF()
    for pin_number in POSTION3:
        GPIO.output (pin_number, LEDON)      
    time.sleep(SPEED)
    ALL_OFF()
    for pin_number in POSTION4:
        GPIO.output (pin_number, LEDON)      
    time.sleep(SPEED)
    ALL_OFF()
    SPEED -= 0.05

for i in range(5):
    for pin_number in POSTION1:
        GPIO.output (pin_number, LEDON)      
    time.sleep(SPEED)
    ALL_OFF()
    for pin_number in POSTION2:
        GPIO.output (pin_number, LEDON)      
    time.sleep(SPEED)
    ALL_OFF()
    for pin_number in POSTION3:
        GPIO.output (pin_number, LEDON)      
    time.sleep(SPEED)
    ALL_OFF()
    for pin_number in POSTION4:
        GPIO.output (pin_number, LEDON)      
    time.sleep(SPEED)
    ALL_OFF()
    SPEED -= 0.05

for i in range(10):
    for pin_number in POSTION1:
        GPIO.output (pin_number, LEDON)      
    time.sleep(SPEED)
    ALL_OFF()
    for pin_number in POSTION2:
        GPIO.output (pin_number, LEDON)      
    time.sleep(SPEED)
    ALL_OFF()
    for pin_number in POSTION3:
        GPIO.output (pin_number, LEDON)      
    time.sleep(SPEED)
    ALL_OFF()
    for pin_number in POSTION4:
        GPIO.output (pin_number, LEDON)      
    time.sleep(SPEED)
    ALL_OFF()
    
GPIO.cleanup()
