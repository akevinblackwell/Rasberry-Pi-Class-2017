from turtle import Turtle, Screen

def checkforclick():
    return


FONTSIZE = 40
FONT = ("Ariel", FONTSIZE, "normal")

turtle1 = Turtle(visible=False)
turtle1.penup()

turtle1.setpos(0, FONTSIZE*2 - FONTSIZE/2)
turtle1.write("1.Option1", align="center", font=FONT)

turtle1.setpos(0, -FONTSIZE/2)
turtle1.write("2.Option2", align="center", font=FONT)

turtle1.setpos(0, -FONTSIZE*2 - FONTSIZE/2)
turtle1.write("3.Option3", align="center", font=FONT)

turtle1.setpos(-200, -200)
turtle1.write("Select an Option", font=FONT)

screen = Screen()
screen.onclick(self.checkforclick)
turtle1.mainloop()

