
'''
Made by Clara Blackwell
7/12/17
Enter a Number and the Program will calculate the factorial.
'''
def factorial(x): # factorial function
    f = x
    for c in range(1,x):
        f = f*(x-c)
    return f


y= int(raw_input("For What Number Do You Want the Factorial: ")) # Asks for the number that you want to factorialize
if y <= 0:      # Defines what is invaild  A.K.A a negative number or zero
    print("Invalid Input; Enter A Positive Number") # Tells you if your input is invalid.
else:
    y = factorial(y)
    print(y)        # Tells you the factorial.
