import time
import RPi.GPIO as GPIO

BlueLED = 3

blinkrate = 0.0

pushbutton = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(BlueLED, GPIO.OUT)

# initialize all LEDs to off

GPIO.output(BlueLED, GPIO.LOW)

# ask for the blinkrate

blinkrate=input("Enter your blinkrate:  ")

while True:
#while GPIO.input(pushbutton) == True:
	GPIO.output(BlueLED, GPIO.HIGH)
	time.sleep(blinkrate)
	GPIO.output(BlueLED, GPIO.LOW)
	time.sleep(blinkrate)
	
#	print GPIO.input(pushbutton)

print "Button Pushed"

# initialize all LEDs to off

GPIO.output(BlueLED, GPIO.LOW)
