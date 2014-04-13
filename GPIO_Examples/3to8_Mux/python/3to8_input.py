import time
import RPi.GPIO as GPIO

#Set up ENABLE to Pin 7
ENABLE = 7
#Set up GPIO Board (Not using Broadcom settings)
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

#Set up pins on GPIO 
GPIO.setup(ENABLE,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

#All Off (ENABLE LOW)
def all_off():
    GPIO.output(ENABLE,GPIO.LOW)
    GPIO.output(12,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    time.sleep(1)

#switch LED 1 on 0 0
def LED0_on():
    GPIO.output(ENABLE,GPIO.HIGH)
    GPIO.output(12,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    time.sleep(1)

#switch LED 2 on 0 1
def LED1_on():
    GPIO.output(ENABLE,GPIO.HIGH)
    GPIO.output(12,GPIO.HIGH)
    GPIO.output(13,GPIO.LOW)
    time.sleep(1)

#switch LED 2 on 1 0
def LED2_on():    
    GPIO.output(ENABLE,GPIO.HIGH)
    GPIO.output(12,GPIO.LOW)
    GPIO.output(13,GPIO.HIGH)
    time.sleep(1)

#switch LED 2 on 1 1
def LED3_on():    
    GPIO.output(ENABLE,GPIO.HIGH)
    GPIO.output(12,GPIO.HIGH)
    GPIO.output(13,GPIO.HIGH)
    time.sleep(1)

#Main Program starts here
#Switch all the LED's off
all_off()
while True:
    n = input("\nWhich light would you like on 1-4? ")
    if n == 0 or n > 4:
        all_off()
    elif n == 1:
        LED0_on()
    elif n == 2:
        LED1_on()
    elif n == 3:
        LED2_on()
    elif n == 4:
        LED3_on()

