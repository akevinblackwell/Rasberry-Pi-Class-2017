import time
import RPi.GPIO as GPIO

Channel1 = 07  # good
Channel2 = 11  # good
Channel3 = 13  # good
Channel4 = 15  # good

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(Channel1, GPIO.OUT)
GPIO.setup(Channel2, GPIO.OUT)
GPIO.setup(Channel3, GPIO.OUT)
GPIO.setup(Channel4, GPIO.OUT)

# initialize all LEDs to off

GPIO.output(Channel1, GPIO.HIGH)  # High equals off!
GPIO.output(Channel2, GPIO.HIGH)  # Low equals on!
GPIO.output(Channel3, GPIO.HIGH)
GPIO.output(Channel4, GPIO.HIGH)

print("Testing Channel 1")
for x in range(0,10):
	GPIO.output(Channel1, GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(Channel1, GPIO.HIGH)
	time.sleep(0.5)

print("Testing Channel 2")
for x in range(0,10):
	GPIO.output(Channel2, GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(Channel2, GPIO.HIGH)
	time.sleep(0.5)

print("Testing Channel 3")
for x in range(0,10):
	GPIO.output(Channel3, GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(Channel3, GPIO.HIGH)
	time.sleep(0.5)

print("Testing Channel 4")
for x in range(0,10):
	GPIO.output(Channel4, GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(Channel4, GPIO.HIGH)
	time.sleep(0.5)

print("End Test")

# initialize all LEDs to off

GPIO.output(Channel1, GPIO.HIGH)  # High equals off!
GPIO.output(Channel2, GPIO.HIGH)  # Low equals on!
GPIO.output(Channel3, GPIO.HIGH)
GPIO.output(Channel4, GPIO.HIGH)
