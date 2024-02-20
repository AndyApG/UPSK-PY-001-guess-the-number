# -*- coding: latin-1 -*-
from random import randint
from time import sleep
from game import *

NUMBER_WINNER = randint(1,100)

player_name = ask_name()
player_guess_list = []
computer_guess_list = []
round_number = 1
winner = False



gretting(player_name)

while winner == False:
    print(f'--Round {round_number}--')

    ask_gess(player_name)
    player_guess = read_gess()
    player_result = qualify_guess(player_guess,NUMBER_WINNER)
    print(player_result)
    player_guess_list.append(player_guess)
    winner = is_winner(player_result)
    if winner:
        break
         
    ask_gess('Computer Player')
    computer_guess = randint(1,100)
    sleep(2)   
    print(computer_guess)
    computer_result = qualify_guess(computer_guess,NUMBER_WINNER)
    computer_guess_list.append(computer_guess)
    print(computer_result)
    is_winner(computer_result)

    round_number+=1

print(f"{player_name}'s guess list", player_guess_list)
print("Computer's guess list", computer_guess_list)