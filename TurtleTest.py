from turtle import Turtle
import time
from TurtleElectronics import turtlepushbutton, turtlediode, turtleled, turtleresistor, turtleground, turtletransistor, turtleactivebuzz


newturtle2 = Turtle()
newturtle2.pensize(2)
#turtleactivebuzz(newturtle2, 0, 20, "black", 0,0)
turtleled(newturtle2, 0, 20, "black", 0,0)

newturtle2.hideturtle()

time.sleep(15)
