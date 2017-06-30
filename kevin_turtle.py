import turtle 

ninja = turtle.Turtle()

ninja.speed(2)

for i in range(180):
    if (i % 2) == 0:
        ninja.pencolor("blue")
    else:
        ninja.pencolor("red")
 
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)
    
turtle.done()
