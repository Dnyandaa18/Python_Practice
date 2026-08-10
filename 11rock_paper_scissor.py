import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer =  random.choice(options)
    print(computer)
        
    while player not in options:
        player = input("Enter your choice(rock, paper, scissors): ").lower()

    if player == computer:
        print("It's a Tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "rock":
        print("You win!")
    else:
        print("Computer win!")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if not play_again == "y":
        running = False
    

print("Thanks for playing!")