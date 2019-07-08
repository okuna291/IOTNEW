#!/usr/bin/env python
import RPi.GPIO as GPIO # require/import RPi.GPIO module from GPIO library 
import time  # require/import time module




##########################################
#simple blink
GPIO.setmode(GPIO.BOARD)  #to use Raspberry Pi board pin numbers  
GPIO.setup(11, GPIO.OUT) #set up GPIO output channel 

#blinking
GPIO.output(11,GPIO.HIGH)# turn GPIO 11 on
time.sleep(2)# wait 2 seconds
GPIO.output(11,GPIO.LOW)# turn GPIO 11 off
time.sleep(2)# wait 2 seconds
GPIO.output(11,GPIO.HIGH)# turn GPIO 11 on


