from DrawX import drawX
import turtle

turtle.setup(800,600)       # specifies the screen size.

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

Xwin = ('XXX######','###XXX###','######XXX')

Owin = ('XXX######','###XXX###','######XXX')

for turn in range(9)
    raw_input()
    if CurrentState in Xwin:
        print("X wins")
        break;
    elif CurrentState in Owin:
        print("O Win")
        break;

if turn = 8:
    print("Cat")
    

CurrentStatus = "........."

"..X......"






tictactoeturtle = turtle.Turtle()
drawX(tictactoeturtle, 0, 0, 50, "black")


