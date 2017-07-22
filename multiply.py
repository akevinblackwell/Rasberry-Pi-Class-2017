##def factorial(n):return reduce(lambda x,y:x*y,[1]+range(1,n+1))

def factorial(x):
    if x == 0:
        return 1
    else:
        return x*factorial(x-1)
        print (factorial(x))
right = True
x = 1
while right:
    try:
        x = int(input("Enter a Number")) 
        print (factorial(x))
        right = False
    except:
        print("You didn't enter a number")
        right = True
##invalidinput = True
##factorialnumber = 1
##while invalidinput:
##    try:
##        factorialnumber = int(input("Enter a positive integer between 1 and 100: "))
##        invalidinput = False
##    except:
##        print("Invalid Input.  Try again.")
##        invalidinput = True
##if x > 100:
##    print('Number '+str(x)+' is too big.')
##elif x >= 1:
##    print('The factorial of '+str(x)+' is '+str(factorial(x)))
##elif x ==0:
##    print('The factorial of '+str(x)+ ' is 1.')
##else:
##    print('The factorial of '+str(x)+ ' is undefined because '+str(x)+' is negative.')
##
##
