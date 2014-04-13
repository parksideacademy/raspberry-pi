import time
import RPi.GPIO as GPIO
 
GPIO.cleanup()
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(12,GPIO.IN)
 
while True:
        GPIO.output(11,GPIO.HIGH)
        if (GPIO.input(12) == True):
                print(“pressed”)
                time.sleep(3)
                GPIO.output(13,GPIO.HIGH)
                time.sleep(3)
                GPIO.output(11,GPIO.LOW)
 
                GPIO.output(11,GPIO.LOW)
                GPIO.output(13,GPIO.LOW)
                GPIO.output(15,GPIO.HIGH)
                time.sleep(3)
                GPIO.output(15,GPIO.LOW)
                GPIO.output(13,GPIO.HIGH)
                time.sleep(3)
                GPIO.output(13,GPIO.LOW)
                print(“End”)
