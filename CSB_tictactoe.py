import turtle
from DrawX import drawX

def fillcell(cellno,XorO):
    if cellno == 1:
        drawX(tictactoeturtle, -120, 120, 50, "black")
    elif cellno == 2:
        drawX(tictactoeturtle, 0, 120, 50, "black")
    elif cellno == 3:
        drawX(tictactoeturtle, 120, 120, 50, "black")
    elif cellno == 4:
        drawX(tictactoeturtle, -120, 0, 50, "black")
    elif cellno == 5:
        drawX(tictactoeturtle, 0, 0, 50, "black")
    elif cellno == 6:
        drawX(tictactoeturtle, 120, 0, 50, "black")
    elif cellno == 7:
        drawX(tictactoeturtle, -120, -120, 50, "black")
    elif cellno == 8:
        drawX(tictactoeturtle, 0, -120, 50, "black")
    elif cellno == 9:
        drawX(tictactoeturtle, 120, -120, 50, "black")
    return

turtle.setup(800,600)       # specifies the screen size.

tictactoeturtle = turtle.Turtle()

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

fillcell(1,True)
fillcell(2,True)
fillcell(3,True)
fillcell(4,True)
fillcell(5,True)
fillcell(6,True)
fillcell(7,True)
fillcell(8,True)
fillcell(9,True)
