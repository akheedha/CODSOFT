import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Choose a option from Rock/Paper/Scissors or type Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
   
    computer_choice = options[random_number]
    print("Computer picked", computer_choice + ".")

    if user_input == "rock" and computer_choice == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_choice == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_choice == "paper":
        print("You won!")
        user_wins += 1 

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
