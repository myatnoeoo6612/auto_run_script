import RPi.GPIO as GPIO
import os
import time
count = 0
LED_PIN = 13
buzzer = 21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(buzzer,GPIO.OUT)

try:
    while True:
        
        while count < 30:
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(0.5)
            count +=1
            ##print(count)
            if count == 30 :
                GPIO.output(buzzer,GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(buzzer,GPIO.LOW)
                time.sleep(0.2)                
                GPIO.output(buzzer,GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(buzzer,GPIO.LOW)
                time.sleep(0.2)
                break
            print(count)
                
        GPIO.output(LED_PIN, GPIO.HIGH) 
        
        ##time.sleep(60)
                
except KeyboardInterrupt:
    GPIO.clearup()
    
                      
                
                
