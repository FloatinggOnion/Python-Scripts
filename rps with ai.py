import random

player_wins = 0
computer_wins = 0
winning_score = input("Best of how many? ")
winning_score = int(winning_score)

while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("Rock...")
    print("Paper...")
    print("Scissors...")

    player = input("Player, make your move, or q to quit: ").lower()
    if player == "q":
        break
    rand_num = random.randint(0,2)

    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    elif rand_num == 2:
        computer = "scissors"

    print(f"Computer plays {computer}   ")

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("player wins!")
            player_wins += 1
        else:
            print("computer wins!")
            computer_wins += 1

    elif player == "paper":
        if computer == "rock":
            print("player wins!")
            player_wins += 1
        else:
            print("computer wins!")
            computer_wins += 1

    elif player == "scissors":
        if computer == "rock":
            print("computer wins!")
            computer_wins += 1
        else:
            print("player wins!")
            player_wins += 1

    else:
        print("Please enter a valid move!")

print(f"FINAL SCORES...Player: {player_wins} Computer: {computer_wins}")

if player_wins > computer_wins:
    print("CONGRATS!! YOU WON!!")
elif player_wins == computer_wins:
    print("TIED GAME!!")
else:
    print("BETTER LUCK NEXT TIME!!")