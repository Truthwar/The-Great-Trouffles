import random

options = ["Rock", "Paper", "Scissor"]
playerScore = 0
computerScore = 0

while(True):
    computer = random.choice(options)
    player = input("Rock, Paper, Scissor? >> ").capitalize()

    if player == "Rock":
        if computer == "Paper":
            print("You lose!!")
            computerScore += 1
        else:
            print("You win!!")
            playerScore += 1
    elif player == "Paper":
        if computer == "Scissor":
            print("You lose!!")
            computerScore += 1
        else:
            print("You Win!!") 
            playerScore += 1
    elif player == "Scissor":
        if computer == "Rock":
            print("You lose!!")
            computerScore += 1
        else: 
            print("You win!!")
            playerScore += 1
    elif player == "End":
        print("Game Over")
        print(f"Computer Score >> {computerScore}")
        print(F"Player Score >> {playerScore}")
        print("Goodbye!")
        break
