## This is the very first code I have written all by myself.  I am still working on hiding the previous player's decision,
##as well as ending after 1 game.

END = False
while not END:
    print ("ROCK, PAPER, SCISSORS, SHOOT")
    p1 = raw_input("Enter Your Name Player 1")
    p2 = raw_input("Enter Your Name Player 2")
    if p1 == "Aidan":
        print ("Welcome Master Aidan.  Good Luck") 
    player1 = raw_input("Enter Either Rock, Paper, or Scissors Player 1")
    player2 =  raw_input("Enter Either Rock, Paper, or Scissors Player 2")  
##    rock << paper
##    rock >> scissors
##    rock == rock
    if player1 == "rock" and player2 == "scissors":
        print ("Player 1 WINS")
    elif player1 == "scissors" and player2 == "rock":
        print ("PLAYER 2 WINS")
    elif player1 == "rock" and player2 == "paper":
        print ("PLAYER 2 WINS")
    elif player1 == "paper" and player2 == "rock":
        print ("PLAYER 1 WINS")
    elif player1 == "paper" and player2 == "scissors":
        print ("PLAYER 2 WINS")
    elif player1 == "scissors" and player2 == "paper":
        print ("PLAYER 1 WINS")
    elif player1 == "rock" and player2 == "rock":
        print ("TIE.  REDO")
    elif player1 == "paper" and player2 == "paper":
        print ("TIE.  REDO")
    elif player1 == "scissors" and player2 == "scissors":
        print ("TIE.  REDO")
    done = raw_input ("Would You Like To Play Again?")
    if done == "yes":
        END = False
    if done == "no":
        END = True
    
       
