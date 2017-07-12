Python 3.4.2 (default, Oct 19 2014, 13:31:11) 
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> END = False
while not END:
    print ("ROCK, PAPER, SCISSORS, SHOOT")
    player1 = raw_input("Enter Either Rock, Paper, or Scissors Player 1")
    player2 =  raw_input("Enter Either Rock, Paper, or Scissors Player 2")
##    rock << paper
##    rock >> scissors
##    rock == rock
    if player1 == "rock" and player2 == "scissors":
        print ("PLAYER 1 WINS")
    else player1 == "scissors" and player2 == "rock":
        print ("PLAYER 2 WINS")
    else player1 == "rock" and player2 == "paper":
        print ("PLAYER 2 WINS")
    else player1 == "paper" and player2 == "rock":
        print ("PLAYER 1 WINS")
    else player1 == "paper" and player2 == "scissors":
        print ("PLAYER 2 WINS")
    else player1 == "scissors" and player2 == "paper":
        print ("PLAYER 1 WINS")
    else player1 == "rock" and player2 == "rock":
        print ("TIE.  REDO")
    else player1 == "paper" and player2 == "paper":
        print ("TIE.  REDO")
    else player1 == "scissors" and player2 == "scissors":
        print ("TIE.  REDO")
        END = True
