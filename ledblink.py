import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)      #Define pin output
GPIO.output(3,0)

while True:
    print("Led on")
    GPIO.output(3,1)
    time.sleep(1)
    
