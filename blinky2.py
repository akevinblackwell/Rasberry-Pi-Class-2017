
# blinky2-C-dawgs's 2nd python program

import time
import RPi.GPIO as GPIO

LED = 22

# config general purpose IO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

# enter blinkrate in seconds

blinkrate = .5		# blinkate = 2x per sec
eventext ="y is even"
# while False:
#		GPIO.output(LED, GPIO.HIGH)
#		time.sleep(blinkrate)
#		GPIO.output(LED, GPIO.LOW)
#		time.sleep(blinkrate)
while True:
	y=input("Enter your number:  ")

#for x in range(0,10,y):
#	print "hello world!"
#	print x
	if (y%2)==0:
		print evensstext
	else:
		print "y is odd"
