from DrawX import drawX
from drawO import drawO
##from pymouse import PyMouseEvent
import turtle

End = True
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

def fillcell(cellno,XorO):
    if cellno == 1:
        drawX(tictactoeturtle, -120, 120, 50, "black")
    elif cellno == 2:
        drawX(tictactoeturtle, 0, 120, 50, "black")
    elif cellno == 3:
        drawX(tictactoeturtle, 120, 120, 50, "black")
    elif cellno == 4:
        drawX(tictactoeturtle, -120, 0, 50, "black")
    elif cellno == 5:
        drawX(tictactoeturtle, 0, 0, 50, "black")
    elif cellno == 6:
        drawX(tictactoeturtle, 120, 0, 50, "black")
    elif cellno == 7:
        drawX(tictactoeturtle, -120, -120, 50, "black")
    elif cellno == 8:
        drawX(tictactoeturtle, 0, -120, 50, "black")
    elif cellno == 9:
        drawX(tictactoeturtle, 120, -120, 50, "black")
    return


while End == True: 
    letter = raw_input("Do you want to be X or O?")
    if letter == "O":
        place = raw_input("Enter a position by detailing all the places before spot as '.'") 
        if place == "1":
            tictactoeturtle = turtle.Turtle()
            drawO(tictactoeturtle, -115,115, 50, "maroon")

    elif letter == "X":
            Place = raw_input("Enter a position by detailing all the places before spot as '.'") 
            if Place == "2":
                tictactoeturtle = turtle.Turtle()
                drawX(tictactoeturtle, 0,115,50, "black")

   
    elif letter == "O":
            pLace = raw_input("Enter a position by detailing all the places before spot as '.'") 
            if pLace == "4":
                tictactoeturtle = turtle.Turtle()
                drawO(tictactoeturtle, -1,78, 50, "maroon")

    elif letter == "X":
            PLace = raw_input("Enter a position by detailing all the places before spot as '.'") 
            if PLace == "3":
                tictactoeturtle = turtle.Turtle()
                drawX(tictactoeturtle, -5,11,50, "black")



        
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


