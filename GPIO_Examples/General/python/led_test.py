import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

GPIO.output(11,GPIO.HIGH)
time.sleep(5)
GPIO.output(11,GPIO.LOW)
GPIO.output(7,GPIO.HIGH)
time.sleep(5)
GPIO.output(7,GPIO.LOW)
