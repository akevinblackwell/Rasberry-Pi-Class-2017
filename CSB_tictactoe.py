import turtle
from ButtonPush import ButtonPush, ButtonPushSetupSetdown
from winnercheck import winnercheck
from DrawX import drawX
from drawO import drawO

def drawXorO(turtleXorO,X,Y,size,color,XorO2):
    if XorO2 == True:
        drawX(tictactoeturtle, X, Y, size, color)
    else:
        drawO(tictactoeturtle, X, Y, size, color)
    return

def fillcell(cellnum,XorO):
    if cellnum == 1:
        drawXorO(tictactoeturtle, -120, 120, 50, "black",XorO)
    elif cellnum == 2:
        drawXorO(tictactoeturtle, 0, 120, 50, "black",XorO)
    elif cellnum == 3:
        drawXorO(tictactoeturtle, 120, 120, 50, "black",XorO)
    elif cellnum == 4:
        drawXorO(tictactoeturtle, -120, 0, 50, "black",XorO)
    elif cellnum == 5:
        drawXorO(tictactoeturtle, 0, 0, 50, "black",XorO)
    elif cellnum == 6:
        drawXorO(tictactoeturtle, 120, 0, 50, "black",XorO)
    elif cellnum == 7:
        drawXorO(tictactoeturtle, -120, -120, 50, "black",XorO)
    elif cellnum == 8:
        drawXorO(tictactoeturtle, 0, -120, 50, "black",XorO)
    elif cellnum == 9:
        drawXorO(tictactoeturtle, 120, -120, 50, "black",XorO)
    return

turtle.setup(800,600)       # specifies the screen size.
tictactoeturtle = turtle.Turtle()

tictactoeturtle.penup()
tictactoeturtle.setposition(-60,60+120)
tictactoeturtle.pendown()
tictactoeturtle.setposition(-60,-60*3)
tictactoeturtle.penup()

tictactoeturtle.penup()
tictactoeturtle.setposition(60,60+120)
tictactoeturtle.pendown()
tictactoeturtle.setposition(60,-60*3)
tictactoeturtle.penup()

tictactoeturtle.penup()
tictactoeturtle.setposition(60+120,-60)
tictactoeturtle.pendown()
tictactoeturtle.setposition(-60*3,-60)
tictactoeturtle.penup()

tictactoeturtle.penup()
tictactoeturtle.setposition(60+120,60)
tictactoeturtle.pendown()
tictactoeturtle.setposition(-60*3,60)
tictactoeturtle.penup()


squares = [".", ".", ".", ".", ".", ".", ".", ".", "."]

x = 0
winnerstatus = '.'

ButtonPushSetupSetdown(True)
while winnerstatus=='.':
#    cell = int(raw_input("CellNo"))  # uncomment if you want to use keyboard instead of buttons.
    cell = ButtonPush()
    
    if squares[cell-1] == ".":  #is the cell empty?
        x = x+1
        if x % 2 == 1:
            fillcell(cell,True)   #drawX
            squares[cell-1] = "X"
        else:
            fillcell(cell,False)   #drawO
            squares[cell-1] = "O"

    winnerstatus = winnercheck(squares)
    if winnerstatus == "X":
        print("X Wins")
    elif winnerstatus == "O":
        print("O Wins")
    elif winnerstatus == "C":
        print("Cat")
    
    print(squares)
        
ButtonPushSetupSetdown(False)
