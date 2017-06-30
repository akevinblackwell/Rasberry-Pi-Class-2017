'''
Written by: Clara Blackwell
January, 2017

Converts numbers and/or letters into their morse translation, then blinks LED accordingly.
'''
#morseinput Dictionary
#'morseinput':'morseoutput'
morse_dict = {'a':'.-',
              'b':'-...',
              'c':'-.-.',
              'd':'-..',
              'e':'.',
              'f':'..-.',
              'g':'--.',
              'h':'....',
              'i':'..',
              'j':'.---',
              'k':'-.-',
              'l':'.-..',
              'm':'--',
              'n':'-.',
              'o':'---',
              'p':'.--.',
              'q':'--.-',
              'r':'.-.',
              's':'...',
              't':'-',
              'u':'..-',
              'v':'...-',
              'w':'.--',
              'x':'-..-',
              'y':'-.--',
              'z':'--..',
              ' ':' ',
              '1':'.----',
              '2':'..---',
              '3':'...--',
              '4':'....-',
              '5':'.....',
              '6':'-....',
              '7':'--...',
              '8':'---..',
              '9':'----.',
              '0':'-----',
              '.':'*'}

# Function to flash LED on and off for a specified time.
def BlinkLED(WhichLED, timeon, timeoff):

    GPIO.output(WhichLED, GPIO.HIGH)     #turn LED on
    time.sleep(timeon)
    GPIO.output(WhichLED, GPIO.LOW)      #turn LED off
    time.sleep(timeoff)
    return

BlueLED = 22

#morseblinkrate speed
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(BlueLED, GPIO.OUT)
GPIO.output(BlueLED, GPIO.LOW)

while True:
        

    #Define morseinput as a string
    morseinput = ""
    morseoutput = ""

    #Asking for morseinput
    morseinput=raw_input("Enter your morseinput (x to quit):  ")
    morseinput = morseinput.lower()
    
    if morseinput == "x":         # if user enters 'x', then quit program.
        break

    #Number of Characters in your morseinput
    morseinputlength = len(morseinput)

    #Converts morseinput to morseoutput
    for x in range(0,morseinputlength,1):
        morseoutput = morseoutput + morse_dict[morseinput[x]]+"/"

    #Speed of dots, dashes, spaces, and stops.
    #Change time_unit
    time_unit = 0.1        #in seconds

    #Blinks LED at a certain speed ans pattern
    print(morseoutput,len(morseoutput))
    for x in range(0,len(morseoutput)):

        ontime = 0.0        #set variables to 0
        offtime = 0.0       
        
        if morseoutput[x] == '.':       #dot pattern
            ontime = time_unit
            offtime = time_unit
        if morseoutput[x] == '-':       #dash pattern
            ontime = time_unit*3
            offtime = time_unit
        if morseoutput[x] == '/':       #end of character pattern
            ontime = time_unit*0
            offtime = time_unit*3
        if morseoutput[x] == '*':       #stop sentence or phrase
            ontime = time_unit*0
            offtime = time_unit*7
        print(ontime,offtime)

        BlinkLED(BlueLED, ontime, offtime)
    
#initialize BlueLED off
GPIO.output(BlueLED, GPIO.LOW)

#cleans up GPIO
GPIO.cleanup()
