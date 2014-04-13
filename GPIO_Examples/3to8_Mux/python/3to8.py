import time
import RPi.GPIO as GPIO

#Set up ENABLE to Pin 7
ENABLE = 7

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

GPIO.setup(ENABLE,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

#All Off (ENABLE LOW)
GPIO.output(ENABLE,GPIO.LOW)
GPIO.output(12,GPIO.LOW)
GPIO.output(13,GPIO.LOW)
time.sleep(1)

while True:

    #switch LED 1 on 0 0
    GPIO.output(ENABLE,GPIO.HIGH)
    GPIO.output(12,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    time.sleep(1)

    #switch LED 2 on 0 1
    GPIO.output(ENABLE,GPIO.HIGH)
    GPIO.output(12,GPIO.HIGH)
    GPIO.output(13,GPIO.LOW)
    time.sleep(1)

    #switch LED 2 on 1 0
    GPIO.output(ENABLE,GPIO.HIGH)
    GPIO.output(12,GPIO.LOW)
    GPIO.output(13,GPIO.HIGH)
    time.sleep(1)

    #switch LED 2 on 1 1
    GPIO.output(ENABLE,GPIO.HIGH)
    GPIO.output(12,GPIO.HIGH)
    GPIO.output(13,GPIO.HIGH)
    time.sleep(1)
