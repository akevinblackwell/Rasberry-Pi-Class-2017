from turtle import Turtle
import time


def turtleactivebuzz(activebuzzturtle, angle, size, color, x, y):
     activebuzzturtle.pencolor(color)
     activebuzzturtle.fillcolor(color)
     activebuzzturtle.penup()

     activebuzzturtle.setposition(x,y-size)           # set position to half size down.
     activebuzzturtle.pendown()
     activebuzzturtle.begin_fill()
     activebuzzturtle.circle(size)
     activebuzzturtle.end_fill()

     activebuzzturtle.penup()
     activebuzzturtle.setposition(x, y - 0.25 * size)     # move position for inside circle
     activebuzzturtle.pencolor("white")
     activebuzzturtle.fillcolor("white")
     activebuzzturtle.begin_fill()
     activebuzzturtle.pendown()

     activebuzzturtle.circle(size*0.25)
     activebuzzturtle.end_fill()

     activebuzzturtle.penup()
     activebuzzturtle.setposition(x, y + 0.25 * size)
     activebuzzturtle.write("+", align="center",font=("arial", 12, "bold") )

     return


def turtleled(ledturtle,angle,size,color,x,y):
     ledturtle.pencolor(color)
     ledturtle.fillcolor(color)
     ledturtle.penup()
     ledturtle.setposition(x,y-size)  # place the circle centered at the cordinate.
     ledturtle.setheading(angle)
     ledturtle.pendown()
     ledturtle.right(angle)
     ledturtle.circle(size)
     ledturtle.penup()
     ledturtle.setposition(x,y)
     ledturtle.setheading(angle)
     ledturtle.forward(size-(size*.5))
     ledturtle.left(90)
     ledturtle.forward(size-(size*.35))
     ledturtle.right(210)
     ledturtle.pendown()
     ledturtle.begin_fill()
     ledturtle.forward(25/20*size)        # triangle side
     ledturtle.right(120)
     ledturtle.forward(25/20*size)        # triangle side
     ledturtle.right(120)
     ledturtle.forward(25/20*size)        # triangle side
     ledturtle.end_fill()
     ledturtle.penup()
     ledturtle.right(90)
     ledturtle.forward(size*1.0)
     ledturtle.left(90)
     ledturtle.pendown()
     ledturtle.backward(size*1.1)

     return

def turtleresistor(resturtle, angle, size, color, x, y):
     resturtle.pencolor(color)

     resturtle.penup()
     resturtle.setposition(x, y)  # place the terminal of the resistor at the coordinates
     resturtle.setheading(angle)
     resturtle.pendown()
     resturtle.forward(size/2)
     resturtle.right(60)
     resturtle.forward(size/2)
     for _ in range(0,3):
         resturtle.left(120)
         resturtle.forward(size/1)
         resturtle.right(120)
         resturtle.forward(size/1)
     resturtle.left(120)
     resturtle.forward(size/2)
     resturtle.right(60)
     resturtle.forward(size/2)

     return

def turtleground(gndturtle, angle, size, color, x, y):
     gndturtle.pencolor(color)

     gndturtle.penup()
     gndturtle.setposition(x, y)  # place the terminal of the resistor at the coordinates
     gndturtle.setheading(angle-90)
     gndturtle.pendown()
     gndturtle.forward(size)
     gndturtle.left(90)
     gndturtle.forward(size)
     gndturtle.backward(size*2)
     gndturtle.penup()
     gndturtle.right(90)
     gndturtle.forward(size/2)
     gndturtle.left(90)
     gndturtle.forward(size/2)
     gndturtle.pendown()
     gndturtle.forward(size)

     gndturtle.penup()
     gndturtle.right(90)
     gndturtle.forward(size/2)
     gndturtle.right(90)
     gndturtle.forward(size/2)
     gndturtle.pendown()
     gndturtle.forward(size/10)

     return

def  turtlepushbutton(pbturtle, angle, size, color, x, y):
     pbturtle.pencolor(color)

     pbturtle.penup()
     pbturtle.setposition(x, y)  # place the terminal of the pushbutton at the coordinates
     pbturtle.setheading(angle - 90)
     pbturtle.pendown()
     pbturtle.forward(size)
     pbturtle.dot(8)
     pbturtle.penup()
     pbturtle.forward(size*2)
     pbturtle.pendown()
     pbturtle.dot(8)

     pbturtle.forward(size)
     pbturtle.penup()
     pbturtle.left(90)
     pbturtle.forward(size)
     pbturtle.left(90)
     pbturtle.forward(size)
     pbturtle.pendown()
     pbturtle.forward(size*2)
     pbturtle.backward(size+3)
     pbturtle.right(90)
     pbturtle.forward(6)
     pbturtle.left(90)
     pbturtle.forward(6)
     pbturtle.left(90)
     pbturtle.forward(6)

     return

def turtletransistor(transistorturtle, angle, size, color, x, y):
     transistorturtle.pencolor(color)
     transistorturtle.fillcolor(color)

     transistorturtle.penup()
     transistorturtle.setposition(x, y)  # place the terminal of the transister at the coordinates
     transistorturtle.setheading(angle - 90)
     transistorturtle.pendown()
     transistorturtle.begin_fill()
     transistorturtle.right(90)
     transistorturtle.forward(size/2)
     transistorturtle.left(90)
     transistorturtle.forward(size)
     transistorturtle.left(90)
     transistorturtle.forward(size)
     transistorturtle.left(90)
     transistorturtle.forward(size)
     transistorturtle.left(90)
     transistorturtle.forward(size/2)
     transistorturtle.end_fill()
     transistorturtle.left(90)
     transistorturtle.penup()
     transistorturtle.forward(size)
     transistorturtle.pendown()
     transistorturtle.forward(size*2)
     transistorturtle.backward(size*2)
     transistorturtle.right(90)
     transistorturtle.forward(size/2)
     transistorturtle.left(90)
     transistorturtle.forward(size*1.5)
     transistorturtle.backward(size*1.5)
     transistorturtle.left(90)
     transistorturtle.forward(size)
     transistorturtle.right(90)
     transistorturtle.forward(size*1.5)

     return

def  turtlediode(diodeturtle, angle, size, color, x, y):
     diodeturtle.pencolor(color)
     diodeturtle.fillcolor(color)

     diodeturtle.penup()
     diodeturtle.setposition(x, y)
     diodeturtle.setheading(angle)
     diodeturtle.forward(size - (size * .4))
     diodeturtle.left(90)
     diodeturtle.forward(size - (size * .3))
     diodeturtle.right(210)
     diodeturtle.pendown()
     diodeturtle.begin_fill()
     diodeturtle.forward(25 / 20 * size)  # triangle side
     diodeturtle.right(120)
     diodeturtle.forward(25 / 20 * size)  # triangle side
     diodeturtle.right(120)
     diodeturtle.forward(25 / 20 * size)  # triangle side
     diodeturtle.end_fill()
     diodeturtle.penup()
     diodeturtle.right(90)
     diodeturtle.forward(size * 1.1)
     diodeturtle.left(90)
     diodeturtle.pendown()
     diodeturtle.backward(size * 1.2)

     return
