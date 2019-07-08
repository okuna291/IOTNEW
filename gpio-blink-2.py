#!/usr/bin/env python
import RPi.GPIO as GPIO # require/import RPi.GPIO module from GPIO library 
import time  # require/import time module




GPIO.setmode(GPIO.BOARD)  #to use Raspberry Pi board pin numbers  
GPIO.setup(11, GPIO.OUT) #set up GPIO output channel   
def blink(pin):  # create "blink" function
        GPIO.output(pin,GPIO.HIGH)  
        time.sleep(1)  
        GPIO.output(pin,GPIO.LOW)  
        time.sleep(1)  
        return  

#blink GPIO11 multiple times  
for i in range(0,5):  
        blink(11)  
GPIO.cleanup()# this ensures a clean exit
