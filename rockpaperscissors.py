# Asks for names
Player1 = raw_input("Player1 Enter Your Name: ")

Player2 = raw_input("Player2 Enter Your Name: ")

done = False

# asks if players choose rock, paper, or scissors or decides to quit.
while not done:
    rockpaperscissors1 = raw_input("Does Player1 choose Rock, Paper, Scissors, or Quit? ")
    rockpaperscissors1 = rockpaperscissors1.lower()
    rockpaperscissors2 = raw_input("Does Player2 choose Rock, Paper, Scissors, or Quit? ")
# defines all inputs and decides the proper output and print who wins or if it were a tie.
    if rockpaperscissors1 == "quit" or rockpaperscissors2 == "quit":
        done = True
        
    elif rockpaperscissors1 == "rock" and rockpaperscissors2 == "rock":
        print("tie")

    elif rockpaperscissors1 == "rock" and rockpaperscissors2 == "scissors":
        print("Player1 wins")

    elif rockpaperscissors1 == "rock" and rockpaperscissors2 == "paper":
        print("Player2 wins")

    elif rockpaperscissors1 == "scissors" and rockpaperscissors2 == "rock":
        print("Player2 wins")

    elif rockpaperscissors1 == "scissors" and rockpaperscissors2 == "scissors":
        print("tie")

    elif rockpaperscissors1 == "scissors" and rockpaperscissors2 == "paper":
        print("Player1 wins")

    elif rockpaperscissors1 == "paper" and rockpaperscissors2 == "rock":
        print("Player1 wins")

    elif rockpaperscissors1 == "paper" and rockpaperscissors2 == "scissors":
        print("Player2 wins")

    elif rockpaperscissors1 == "paper" and rockpaperscissors2 == "paper":
        print("tie")

    else:
        print("Error")
