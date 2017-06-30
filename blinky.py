import time
import RPi.GPIO as GPIO

BlueLED = 22
RedLED = 15
GreenLED = 13
YellowLED = 11

blinkrate = 0.0

pushbutton = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(BlueLED, GPIO.OUT)
GPIO.setup(RedLED, GPIO.OUT)
GPIO.setup(GreenLED, GPIO.OUT)
GPIO.setup(YellowLED, GPIO.OUT)
GPIO.setup(pushbutton, GPIO.IN)

# initialize all LEDs to off

GPIO.output(BlueLED, GPIO.LOW)
GPIO.output(RedLED, GPIO.LOW)
GPIO.output(GreenLED, GPIO.LOW)
GPIO.output(YellowLED, GPIO.LOW)

# ask for the blinkrate

blinkrate=input("Enter your blinkrate:  ")

while True:
#while GPIO.input(pushbutton) == True:
	GPIO.output(BlueLED, GPIO.HIGH)
	GPIO.output(RedLED, GPIO.LOW)
	GPIO.output(GreenLED, GPIO.LOW)
	GPIO.output(YellowLED, GPIO.LOW)
	time.sleep(blinkrate)
	GPIO.output(BlueLED, GPIO.LOW)
	GPIO.output(RedLED, GPIO.HIGH)
	GPIO.output(GreenLED, GPIO.LOW)
	GPIO.output(YellowLED, GPIO.LOW)
	time.sleep(blinkrate)
	GPIO.output(BlueLED, GPIO.LOW)
	GPIO.output(RedLED, GPIO.LOW)
	GPIO.output(GreenLED, GPIO.HIGH)
	GPIO.output(YellowLED, GPIO.LOW)
	time.sleep(blinkrate)
	GPIO.output(BlueLED, GPIO.LOW)
	GPIO.output(RedLED, GPIO.LOW)
	GPIO.output(GreenLED, GPIO.LOW)
	GPIO.output(YellowLED, GPIO.HIGH)
	time.sleep(blinkrate)
#	print GPIO.input(pushbutton)

print "Button Pushed"

# initialize all LEDs to off

GPIO.output(BlueLED, GPIO.LOW)
GPIO.output(RedLED, GPIO.LOW)
GPIO.output(GreenLED, GPIO.LOW)
GPIO.output(YellowLED, GPIO.LOW)
