'''
      ButtonPush() - a function to check the status of our TicTacToe buttons
      and return a cell number if one is pushed.

      ButtonPushSetupSetdown(True/False) - a function that configures the GPIO pins.  Call it once with True to start.
      Call again when done with False.
'''

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.IN)

while True:    # while no button pushed yet,
     print(GPIO.input(3))

