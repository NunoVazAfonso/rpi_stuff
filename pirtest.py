import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
##GPIO.setup(3,GPIO.OUT)      #Define LED pin output
GPIO.setup(11,GPIO.IN)     #PIR motion detector

##def led_status(status = 0):
##    GPIO.output(3,status)

##led_status(0)

intruder_count = 0

while True:
    #led_status(0) # turn led off by default
    
    motion_sensor = GPIO.input(11)
    
    if motion_sensor == 1:
        ##led_status(1)
        print "Intruder detected ", intruder_count
        intruder_count += 1
        time.sleep(1)
        
    elif motion_sensor == 0:
        ##led_status(0)
        print "nothing "
        time.sleep(1)
    
    
