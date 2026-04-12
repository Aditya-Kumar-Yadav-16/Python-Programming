# ROCK PAPER SCISSORS GAME

"""
WORKFLOW OF THE PROJECT
1. Input from User (Rock, Paper, Scissors)
2. Computer's Choice (Randomly Generated)
3. Result print 

Cases:
A Rock 
- Rock vs Rock = Tie
- Rock vs Paper = Paper Wins
- Rock vs Scissors = Rock Wins
B Paper
- Paper vs Rock = Paper Wins
- Paper vs Paper = Tie
- Paper vs Scissors = Scissors Wins
C Scissors
- Scissors vs Rock = Rock Wins
- Scissors vs Paper = Scissors Wins
- Scissors vs Scissors = Tie

"""

import random
item_list = ["rock", "paper", "scissors"]

user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
computer_choice = random.choice(item_list)
print(f"User's Choice: {user_choice}")
print(f"Computer's choice: {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
    print("Congratulations! You win!")
else:
    print("Sorry! Computer wins!")