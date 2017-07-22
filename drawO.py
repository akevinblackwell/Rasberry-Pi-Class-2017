import time, turtle


def drawO(Oturtle, x, y, d, color):
     Oturtle.pencolor(color)
     Oturtle.fillcolor(color)
     Oturtle.penup()

     Oturtle.setposition(x,y-d)
     Oturtle.pendown()
     Oturtle.begin_fill()
     Oturtle.circle(d)
     Oturtle.end_fill()

     Oturtle.setposition(x,y+25-d)
     Oturtle.begin_fill()
     Oturtle.fillcolor("white")
     Oturtle.circle(d*0.75)
     Oturtle.end_fill()

     return

turtle.setup(400,300)

tictactoeturtle = turtle.Turtle()
drawO(tictactoeturtle, 0,0, 100, "black")
