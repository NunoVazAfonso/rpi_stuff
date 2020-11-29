from picamera import PiCamera
from datetime import datetime
from subprocess import call

import RPi.GPIO as GPIO
import time
import os


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)    
GPIO.setup(11,GPIO.IN)      #PIR motion detector

#configs
gpio_pir_input = 11 # input GPIO pin nr
video_local_destination = '/home/pi/camera_module/videos/got_you'

intruder_count = 0

camera = PiCamera(resolution = '720p' , framerate = 30)

is_recording = False

time.sleep(5)

while True:

    motion_sensor = GPIO.input(gpio_pir_input)
    
    if motion_sensor == 1:

        if is_recording == False :
            is_recording = True
            camera_time = datetime.now().strftime("%d-%b-%Y_%H_%M_%S")
            camera.start_preview(alpha = 200)
            camera.annotate_text = camera_time
            camera.start_recording(video_local_destination + camera_time + '.h264')
            print "Recording started ", 
            time.sleep(10) # record for 10 secs when movement detected
            intruder_count += 1
            print "Movement detected ", intruder_count
            
        time.sleep(1)
        
    elif motion_sensor == 0:
        
        if is_recording == True:    
            print "Movement stopped"
            camera.stop_recording()
            command = "MP4Box -add " + video_local_destination + camera_time + '.h264' + " " +video_local_destination + camera_time + '.mp4'
            call( [command], shell=True )
            os.remove(video_local_destination + camera_time + '.h264')
            print "Recording stopped"
            camera.stop_preview()
            is_recording = False
        
        time.sleep(1)

