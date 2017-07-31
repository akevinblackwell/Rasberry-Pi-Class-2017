import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

pin_to_circuit = 3

GPIO.setup(pin_to_circuit, GPIO.IN)
while (GPIO.input(pin_to_circuit) == GPIO.HIGH):
    print("asdf")
GPIO.cleanup()
## 10 is 19 
