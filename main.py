# -*- coding: latin-1 -*-
from time import sleep
from game import *

# Selecting the number winner randomly

NUMBER_WINNER = random(1,100)

# Ask the name of player
player_name = ask_name()

# Defining the list to save the guess of the players and computer 
player_guess_list = []
computer_guess_list = [0]

# Couter of rounds
round_number = 1

# The variable winnwer is the answer to function is_winner 
# by default there are not winner because the game is not start yet
winner = False


gretting(player_name)

while winner == False:
    # Show the number of round
    print(f'--Round {round_number}--')
    # Ask the guess of the player
    ask_guess(player_name)
    # Save the player's guess in the variable players_guess
    player_guess = read_guess()
    # Compare the number winner with the guess and save the result in player_result
    player_result = qualify_guess(player_guess,NUMBER_WINNER)
    # Wait two seconds and show the result
    sleep(2)  
    print(player_result)
    # Add the guess to the list of player's guesse
    player_guess_list.append(player_guess)
    # Verify if the user won and update the value of winner  
    winner = is_winner(player_result)
    # If the user is the winner print her list of guesses 
    # and ask if she want to play again
    if winner:
        print(f"{player_name}'s guess list", player_guess_list)
        print("Computer's guess list", computer_guess_list[1:])
        play_q = input("Play again? ",)
        new_game(play_q)
        break
         
    sleep(2)  
    # Do the guess of computer and wait 2 seconds to show it
    ask_guess('Computer Player')
    #computer_guess = random(1,100)
    #computer_guess = middle_point(computer_guess_list[-1],player_guess_list[-1]) 
    computer_guess = select_random(computer_guess_list[-1]+1,player_guess_list[-1]) 
    sleep(2) 
    print(computer_guess)
    # Compare the guess whit the number winner and save the reult in computer_result
    computer_result = qualify_guess(computer_guess,NUMBER_WINNER)
    # Add the guess to the list of Computer's guesses and wait 2 seconds
    computer_guess_list.append(computer_guess)
    sleep(2) 
    print(computer_result)
    # Verify if the computer won
    winner = is_winner(computer_result)
    if winner:
        print(f"{player_name}'s guess list", player_guess_list)
        print("Computer's guess list", computer_guess_list[1:])
        play_q = input("Play again? ",)
        new_game(play_q)
        break

    round_number+=1

