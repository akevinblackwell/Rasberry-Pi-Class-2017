import turtle,time

from TurtleElectronics import turtleled,\
     turtleresistor,turtleground,turtleactivebuzz,turtletransistor

turtle.setup(800,600)       # specifies the screen size.

# 

morsescreen = turtle.Screen()
#morsescreen.bgcolor("lightgreen")
morsescreen.title("Morse Wiring Drawing")

morseturtle = turtle.Turtle()

# use TurtleElectronics.py to create electrical components.
  
turtleled(morseturtle,0,20,"blue",-80,30)
turtleresistor(morseturtle,0,15,"black",-70,80)
turtleresistor(morseturtle,0,15,"black",50,-100)
turtleactivebuzz(morseturtle,0,20,"black",80,30)
turtletransistor(morseturtle,0,20,"black",119,-30)
turtleground(morseturtle,0,20,"black",160,-120)
turtleground(morseturtle,0,20,"black",-80,-120)

morseturtle.penup()
morseturtle.setposition(-80,50)
morseturtle.pendown()
morseturtle.setposition(-80,80)
morseturtle.setposition(-70,80)
morseturtle.penup()
morseturtle.setposition(-5,80)
morseturtle.pendown()
morseturtle.pencolor("blue")
morseturtle.setposition(20,80)
morseturtle.penup()
morseturtle.setposition(20,100)
morseturtle.pendown()
morseturtle.setposition(20,-100)
morseturtle.setposition(58,-100)
morseturtle.penup()
morseturtle.pencolor("black")
morseturtle.setposition(115,-100)
morseturtle.pendown()
morseturtle.setposition(119,-100)
morseturtle.setposition(119,-90)
morseturtle.penup()

morseturtle.setposition(80,20)
morseturtle.pendown()
morseturtle.setposition(80,-81)
morseturtle.setposition(110,-81)
morseturtle.penup()

morseturtle.setposition(130,-81)
morseturtle.pendown()
morseturtle.setposition(160,-81)
morseturtle.setposition(160,-120)
morseturtle.penup()
morseturtle.setposition(-80,10)
morseturtle.pendown()
morseturtle.setposition(-80,-120)
morseturtle.penup()
morseturtle.pencolor("red")
morseturtle.setposition(80,50)
morseturtle.pendown()
morseturtle.setposition(80,100)
morseturtle.pencolor("black")

morseturtle.penup()   
morseturtle.setposition(0,200)
morseturtle.write("Morse Code Wiring Diagram",align = "center",font = ("Arial",16,"bold"))

morseturtle.pencolor("red")
morseturtle.setposition(80,110)
morseturtle.write("Vcc (5v)",align = "center",font = ("Arial",12,"normal"))

morseturtle.pencolor("black")
morseturtle.setposition(-60,85)
morseturtle.write("220 Ohm",align = "center",font = ("Arial",12,"normal"))

morseturtle.setposition(70,-125)
morseturtle.write("10k Ohm",align = "center",font = ("Arial",12,"normal"))

morseturtle.setposition(40,100)
morseturtle.begin_fill()
morseturtle.pendown()
morseturtle.forward(40)
morseturtle.right(90)
morseturtle.forward(20)
morseturtle.right(90)
morseturtle.forward(40)
morseturtle.right(90)
morseturtle.forward(20)
morseturtle.end_fill()

morseturtle.setposition(20,100)
morseturtle.pencolor("orange")
morseturtle.write("25",align = "center",font = ("Arial",10,"bold"))


morseturtle.penup()
morseturtle.setposition(0,-240)
morseturtle.pencolor("green")
morseturtle.write("Name:  Clara Blackwell", align="center", font = ("Arial",12,"bold"))
morseturtle.setposition(0,-260)
morseturtle.write("Class:  Python Programming with the Raspberry Pi", align="center", font = ("Arial",12,"bold"))
morseturtle.setposition(0,-280)
morseturtle.write("Date:  February 27, 2017", align="center", font = ("Arial",12,"bold"))




morseturtle.hideturtle()

raw_input("Wait...")

