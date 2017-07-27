'''
drawO function for tic tac toe

drawO(Oturtle, x, y, d, color)

where
     Oturtle is the turtle used to draw
     x - is horizontal coordinate
     y - is verticle coordinate
     d - is diameter of O

'''


import turtle


def drawO(Oturtle, x, y, d, color):
     Oturtle.pencolor(color)
     Oturtle.fillcolor(color)
     Oturtle.penup()

     Oturtle.setposition(x,y-d)
     Oturtle.pendown()
     Oturtle.begin_fill()
     Oturtle.circle(d)
     Oturtle.end_fill()

     Oturtle.setposition(x,y+15-d)
     Oturtle.begin_fill()
     Oturtle.fillcolor("white")
     Oturtle.circle(d*0.75)
     Oturtle.end_fill()

     return

##turtle.setup(400,300)
##
##tictactoeturtle = turtle.Turtle()
##drawO(tictactoeturtle, 0,0, 100, "maroon")
