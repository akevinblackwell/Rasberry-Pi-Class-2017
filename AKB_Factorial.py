'''
    Filenamem:  AKB_Factorial.py
    Author:  Kevin Blackwell
    Date Created:  07/03/2017
    Date last modified:  07/03/2017
    Python Version 3.5

'''
#
# This is a recursive function to calculate the factorial of a positive integer.
#
def factorial(x):
    if x == 1:
        fact = 1
    else:
        fact = x * factorial(x-1)
    return fact
#
# Ask the user for an integer.  Use try/except and a while look to keep asking until
# they give you one.
#
invalidinput = True
factorialnumber = 1
while invalidinput:
    try:
        factorialnumber = int(input("Enter a positive integer between 1 and 100: "))
        invalidinput = False
    except:
        print("Invalid Input.  Try again.")
        invalidinput = True
#
# Now you have an integer but must confirm that it is positive and not zero.  Also that it
# is reasonable since caculating factorials gets ridiculous past about 13
#
if factorialnumber > 100:
    print('Number '+str(factorialnumber)+' is too big.')
elif factorialnumber >= 1:
    print('The factorial of '+str(factorialnumber)+' is '+str(factorial(factorialnumber)))
elif factorialnumber ==0:
    print('The factorial of '+str(factorialnumber)+ ' is 1.')
else:
    print('The factorial of '+str(factorialnumber)+ ' is undefined because '+str(factorialnumber)+' is negative.')
