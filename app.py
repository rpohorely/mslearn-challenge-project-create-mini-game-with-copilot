# Rock-Scissors-Paper game
#
# Game rules:
#   Rock beats Scissors
#   Scissors beats Paper
#   Paper beats Rock
#   If both players choose the same, it's a tie
# 
# The game is played in the console
# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option
# The computer will randomly choose one of the three options
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the computer
# By the end of each round, the player can choose whether to play again or quit the game
# Display the player's score at the end of the game
# The game must handle user inputs, putting them in lowercase and informing the user if the option is invalid
# The winner will be displayed in the console

import random

def get_user_choice():
    user_choice = input('Enter rock, paper, or scissors: ')
    if user_choice.lower() not in ['rock', 'paper', 'scissors']:
        print('Invalid choice. Please enter rock, paper, or scissors.')
        return get_user_choice()
    return user_choice.lower()

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    if user_choice == 'rock':
        return 'win' if computer_choice == 'scissors' else 'lose'
    if user_choice == 'scissors':
        return 'win' if computer_choice == 'paper' else 'lose'
    if user_choice == 'paper':
        return 'win' if computer_choice == 'rock' else 'lose'

def play_game():
    rounds = 0
    user_score = 0
    computer_score = 0
    while True:
        rounds += 1
        print(f'Round: {rounds}')
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = get_winner(user_choice, computer_choice)
        if winner == 'win':
            user_score += 1
        elif winner == 'lose':
            computer_score += 1
        print(f'You chose {user_choice}. The computer chose {computer_choice}. You {winner}.')
        print(f'Score: You {user_score} - {computer_score} Computer')
        play_again = input('Do you want to play again? (yes/no): ')
        if play_again.lower() not in ['yes', 'y']:
            print(f'Total rounds played: {rounds}')
            print(f'Final score: You {user_score} - {computer_score} Computer')
            break

play_game()