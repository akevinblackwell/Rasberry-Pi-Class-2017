'''
      ButtonPush() - a function to check the status of our TicTacToe buttons
      and return a cell number if one is pushed.

      ButtonPushSetupSetdown(True/False) - a function that configures the GPIO pins.  Call it once with True to start.
      Call again when done with False.
'''

import RPi.GPIO as GPIO

# a function to intialize or stop the GPIO.

def ButtonPushSetupSetdown(StartStop):
    if StartStop:
        GPIO.setmode(GPIO.BOARD)

    # A list of pin numbers for the GPIO inputs we are using.
        cells = (3,5,7,29,31,26,24,21,19)

        # First, configure the pins for input.
        for x in range(0,9):
            GPIO.setup(cells[x], GPIO.IN)
    else:
        GPIO.cleanup()            # clean up all GPIO.
    return

# a function to check for button push.
def ButtonPush():

# cellbutton holds a number for the button pushed.  It is zero until then .
    cellbutton = 0

# A list of pin numbers for the GPIO inputs we are using.
    cells = (3,5,7,29,31,26,24,21,19)

    
    while cellbutton == 0:    # while no button pushed yet,
        for x in range(0,9):  # check each pin to see if it is LOW.
             if   GPIO.input(cells[x]) == GPIO.LOW:
                cellbutton = x # if it is, cell cell button equal to the cell number

    return cellbutton+1         # return the cell button.

## OLD CODE FOR REFERENCE

##    cell1 = 3
##    cell2 = 5
##    cell3 = 7
##    cell4 = 29
##    cell5 = 31
##    cell6 = 26
##    cell7 = 24
##    cell8 = 21
##    cell9 = 19
##
##    GPIO.setup(cell1, GPIO.IN)
##    GPIO.setup(cell2, GPIO.IN)
##    GPIO.setup(cell3, GPIO.IN)
##    GPIO.setup(cell4, GPIO.IN)
##    GPIO.setup(cell5, GPIO.IN)
##    GPIO.setup(cell6, GPIO.IN)
##    GPIO.setup(cell7, GPIO.IN)
##    GPIO.setup(cell8, GPIO.IN)
##    GPIO.setup(cell9, GPIO.IN)
##
##    cellbutton = 0
##    while cellbutton == 0:
##        if   GPIO.input(cell1) == GPIO.LOW:
##            cellbutton = 1
##        elif GPIO.input(cell2) == GPIO.LOW:
##            cellbutton = 2
##        elif GPIO.input(cell3) == GPIO.LOW:
##            cellbutton = 3
##        elif GPIO.input(cell4) == GPIO.LOW:
##            cellbutton = 4
##        elif GPIO.input(cell5) == GPIO.LOW:
##            cellbutton = 5
##        elif GPIO.input(cell6) == GPIO.LOW:
##            cellbutton = 6
##        elif GPIO.input(cell7) == GPIO.LOW:
##            cellbutton = 7
##        elif GPIO.input(cell8) == GPIO.LOW:
##            cellbutton = 8
##        elif GPIO.input(cell9) == GPIO.LOW:
##            cellbutton = 9
##ButtonPushSetupSetdown(True)
##while True:
##    print(ButtonPush())
##ButtonPushSetupSetdown(False)
##
