import time
import RPi.GPIO as GPIO

BlueLED = 22
RedLED = 15
GreenLED = 13
YellowLED = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(BlueLED, GPIO.OUT)
GPIO.setup(RedLED, GPIO.OUT)
GPIO.setup(GreenLED, GPIO.OUT)
GPIO.setup(YellowLED, GPIO.OUT)

BlueLED_Obj = GPIO.PWM(BlueLED,  50)
RedLED_Obj = GPIO.PWM(RedLED, 50)
GreenLED_Obj = GPIO.PWM(GreenLED, 50)
YellowLED_Obj = GPIO.PWM(YellowLED, 50)

BlueLED_Obj.start(20)
RedLED_Obj.start(20)
GreenLED_Obj.start(20)
YellowLED_Obj.start(20)

time.sleep(5)

BlueLED_Obj.ChangeDutyCycle(40)
RedLED_Obj.ChangeDutyCycle(40)
GreenLED_Obj.ChangeDutyCycle(40)
YellowLED_Obj.ChangeDutyCycle(40)

time.sleep(5)

BlueLED_Obj.ChangeDutyCycle(60)
RedLED_Obj.ChangeDutyCycle(60)
GreenLED_Obj.ChangeDutyCycle(60)
YellowLED_Obj.ChangeDutyCycle(60)

time.sleep(5)

BlueLED_Obj.ChangeDutyCycle(80)
RedLED_Obj.ChangeDutyCycle(80)
GreenLED_Obj.ChangeDutyCycle(80)
YellowLED_Obj.ChangeDutyCycle(80)

time.sleep(5)

BlueLED_Obj.stop()
RedLED_Obj.stop()
GreenLED_Obj.stop()
YellowLED_Obj.stop()

raw_input("wait...")

BlueLED_Obj.start(0)

while True:
    for x in range(0,100,5):
         BlueLED_Obj.ChangeDutyCycle(x)
    for x in range(100,0,5):
         BlueLED_Obj.ChangeDutyCycle(x)

GPIO.cleanup()
