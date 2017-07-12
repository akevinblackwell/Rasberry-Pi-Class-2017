##THIS IS THE ONE THAT WORKS

END = False
while not END:
    print ("ROCK, PAPER, SCISSORS, SHOOT")
    p1 = raw_input("Enter Your Name Player 1")
    p2 = raw_input("Enter Your Name Player 2")
    if p1 == "Aidan":
        print ("Welcome Master Aidan.  Good Luck") 
    player1 =  raw_input("Enter Either Rock, Paper, or Scissors Player 1")
    player1 = player1.lower() 
    player2 =  raw_input("Enter Either Rock, Paper, or Scissors Player 2")
    player2 = player2.lower()
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
    elif done == "no":
        END = True
    else:
        print ("WRONG ANSWER. HAW HAW HAW HAW HAW HAW HAW HAW HAW HAW HAW HAW HAW HAW HAW HAWWWWWWWWWWW.......")
        END = True
    
       
