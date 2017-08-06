import RPi.GPIO as GPIO

def ButtonPush():
    GPIO.setmode(GPIO.BOARD)

    cell1 = 3
    cell2 = 5
    cell3 = 7
    cell4 = 29
    cell5 = 31
    cell6 = 26
    cell7 = 24
    cell8 = 21
    cell9 = 19

    GPIO.setup(cell1, GPIO.IN)
    GPIO.setup(cell2, GPIO.IN)
    GPIO.setup(cell3, GPIO.IN)
    GPIO.setup(cell4, GPIO.IN)
    GPIO.setup(cell5, GPIO.IN)
    GPIO.setup(cell6, GPIO.IN)
    GPIO.setup(cell7, GPIO.IN)
    GPIO.setup(cell8, GPIO.IN)
    GPIO.setup(cell9, GPIO.IN)

    cellbutton = 0
    while cellbutton == 0:
        if   GPIO.input(cell1) == GPIO.LOW:
            cellbutton = 1
        elif GPIO.input(cell2) == GPIO.LOW:
            cellbutton = 2
        elif GPIO.input(cell3) == GPIO.LOW:
            cellbutton = 3
        elif GPIO.input(cell4) == GPIO.LOW:
            cellbutton = 4
        elif GPIO.input(cell5) == GPIO.LOW:
            cellbutton = 5
        elif GPIO.input(cell6) == GPIO.LOW:
            cellbutton = 6
        elif GPIO.input(cell7) == GPIO.LOW:
            cellbutton = 7
        elif GPIO.input(cell8) == GPIO.LOW:
            cellbutton = 8
        elif GPIO.input(cell9) == GPIO.LOW:
            cellbutton = 9

    GPIO.cleanup()

    return cellbutton

print(ButtonPush())
