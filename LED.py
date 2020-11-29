import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

i = 1

while i < 10:
	print "LED on"
	GPIO.output(18,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(18,GPIO.LOW)
	print "LED off"
	time.sleep(1)
	i+=1
