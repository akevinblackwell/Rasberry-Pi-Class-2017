'''
     drawX function for tic tac toe.

     drawX(Xturtle, x, y, d, color):drawX(Xtu

     where
         Xturtle is the turtle used to draw
         x - is horizontal coordinate
         y - is veritcle coordinate
         d - diameter of the X
         color is "red", "blue" or "green"
         
'''
import turtle

def drawX(Xturtle, x, y, d, color):
     Xturtle.pencolor(color)
     Xturtle.fillcolor(color)
     Xturtle.penup()

     Xturtle.pensize(10)
     
     Xturtle.setposition(x+d, y+d)           # set position to half size down.
     Xturtle.pendown()
     Xturtle.setposition(x-d, y-d)  
     Xturtle.penup()
     Xturtle.setposition(x+d, y-d)           # set position to half size down.
     Xturtle.pendown()
     Xturtle.setposition(x-d, y+d)

     return



