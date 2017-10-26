import time
import RPi.GPIO as GPIO

BlueLED = 3

blinkrate = 1.0

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(BlueLED, GPIO.OUT)



while True:
    GPIO.output(BlueLED, GPIO.HIGH)
    time.sleep(blinkrate)
    GPIO.output(BlueLED, GPIO.LOW)
    time.sleep(blinkrate) 
    
    
