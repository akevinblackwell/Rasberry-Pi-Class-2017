from DrawX import drawX
from drawO import drawO
from pymouse import PyMouseEvent
import turtle


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


letter = raw_input("Do you want to be X or O?")


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


