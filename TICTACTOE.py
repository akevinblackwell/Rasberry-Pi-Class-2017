from DrawX import drawX
from drawO import drawO
from ButtonPush import ButtonPush, ButtonPushSetupSetdown
##from pymouse import PyMouseEvent
import turtle

tictactoeturtle = turtle.Turtle()

def drawXorO(turtleXorO, X, Y, size, color, XorO2):
    if XorO2 == True:
        drawX(tictactoeturtle, X, Y, size, color)
    else:
        drawO(tictactoeturtle, X, Y, size, color)
    return


def fillcell(cellno,XorO):
    if cellno == 1:
        drawXorO(tictactoeturtle, -120, 120, 50, "black", XorO)
    elif cellno == 2:
        drawXorO(tictactoeturtle, 0, 120, 50, "black", XorO)
    elif cellno == 3:
        drawXorO(tictactoeturtle, 120, 120, 50, "black", XorO)
    elif cellno == 4:
        drawXorO(tictactoeturtle, -120, 0, 50, "black", XorO)
    elif cellno == 5:
        drawXorO(tictactoeturtle, 0, 0, 50, "black", XorO)
    elif cellno == 6:
        drawXorO(tictactoeturtle, 120, 0, 50, "black", XorO)
    elif cellno == 7:
        drawXorO(tictactoeturtle, -120, -120, 50, "black", XorO)
    elif cellno == 8:
        drawXorO(tictactoeturtle, 0, -120, 50, "black", XorO)
    elif cellno == 9:
        drawXorO(tictactoeturtle, 120, -120, 50, "black", XorO)
    return

End = True
turtle.setup(400,300)       ## specifies the screen size.

turtle.penup()
turtle.setposition(-60,60+120)
turtle.pendown()
turtle.setposition(-60,-60*3)
turtle.penup()

turtle.penup()
turtle.setposition(60,60+120)
turtle.pendown()
turtle.setposition(60,-60*3)
turtle.penup()

turtle.penup()
turtle.setposition(60+120,-60)
turtle.pendown()
turtle.setposition(-60*3,-60)
turtle.penup()

turtle.penup()
turtle.setposition(60+120,60)
turtle.pendown()
turtle.setposition(-60*3,60)
turtle.penup()

xwin1 = ["X", "X", "X", "#", "#", "#", "#", "#", "#"] 
xwin2 = ["#", "#", "#", "X", "X", "X", "#", "#", "#"]
xwin3 = ["#", "#", "#", "#", "#", "#", "X", "X", "X"]
xwin4 = ["X", "#", "#", "X", "#", "#", "X", "#", "#"]
xwin5 = ["#", "X", "#", "#", "X", "#", "#", "X", "#"]
xwin6 = ["#", "#", "X", "#", "#", "X", "#", "#", "X"]
xwin7 = ["X", "#", "#", "#", "X", "#", "#", "#", "X"]
xwin8 = ["#", "#", "X", "#", "X", "#", "X", "#", "#"]

owin1 = ["X", "X", "X", "#", "#", "#", "#", "#", "#"] 
owin2 = ["#", "#", "#", "X", "X", "X", "#", "#", "#"]
owin3 = ["#", "#", "#", "#", "#", "#", "X", "X", "X"]
owin4 = ["X", "#", "#", "X", "#", "#", "X", "#", "#"]
owin5 = ["#", "X", "#", "#", "X", "#", "#", "X", "#"]
owin6 = ["#", "#", "X", "#", "#", "X", "#", "#", "X"]
owin7 = ["O", "#", "#", "#", "O", "#", "#", "#", "O"]
owin8 = ["#", "#", "X", "#", "X", "#", "X", "#", "#"]

squares = [".", ".", ".", ".", ".", ".", ".", ".", "."]

x = 0

ButtonPushSetupSetdown(True)
while True:
##    cell = ButtonPush()
    cell = int(raw_input("CELLNO>$"))
    if squares[cell-1] ==".":
        x = x+1
        if x %2 == 1:
            fillcell(cell,True)
            squares[cell-1] = "X"
        else:
            fillcell(cell, False)
            squares[cell-1] = "O"
        for square in squares:
            if square == ".":
                exit
            else:
                print "CAT"
        print(squares)
        
    
ButtonPushSetupSetdown(False) 



##tictactoeturtle = turtle.Turtle()
##while End == True: 
##    letter = raw_input("Do you want to be X or O?")
##    if letter == "O":
##        place = raw_input("Enter a position by detailing all the places before spot as '.'") 
##        if place == "1":
##            drawO(tictactoeturtle, -115,115, 50, "maroon")
##        elif place == '2':
##            drawO(tictactoeturtle, 0,115,50, "black")
####        elif place == "2":
####           drawX(tictactoeturtle, 0,115,50, "black")
##        elif place == "3":
##           drawO(tictactoeturtle, 115,115,50, "black")
##                 
##    elif letter == "X":
##        place = raw_input("Enter a position by detailing all the places before spot as '.'") 
##        if place == "1":
##            drawX(tictactoeturtle, -115,115, 50, "maroon")
##        elif place == "2":
##            drawX(tictactoeturtle, 0,115,50, "black")
####
##   
##    elif letter == "O":
##            pLace = raw_input("Enter a position by detailing all the places before spot as '.'") 
##            if pLace == "4":
##                tictactoeturtle = turtle.Turtle()
##                drawO(tictactoeturtle, -1,78, 50, "maroon")
##
##    elif letter == "X":
##            PLace = raw_input("Enter a position by detailing all the places before spot as '.'") 
##            if PLace == "3":
##                tictactoeturtle = turtle.Turtle()
##                drawX(tictactoeturtle, -5,11,50, "black")



        
Xwin = ('XXX######','###XXX###','######XXX')

Owin = ('XXX######','###XXX###','######XXX')

CurrentState = "........."

"..X......"

for turn in range(9): 
    raw_input("Enter your X/O in a spot by detailing all the spots before it except yours as #")
    if CurrentState in Xwin:
        print("X wins")
        break;
    elif CurrentState in Owin:
        print("O Win")
        break;

if turn == 8:
    print("Cat")
    







tictactoeturtle = turtle.Turtle()
drawX(tictactoeturtle, 0, 0, 50, "black")
drawO(tictactoeturtle, 0, 0, 50, "red")


