import turtle
from ButtonPush import ButtonPush

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


print("BLAH")
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

for x in range(0,9):
    cell = ButtonPush()
    if not x in (1,3,5,7,9):
        fillcell(cell,True)
    else:
        fillcell(cell,False)




