# -*- coding: latin-1 -*-
from random import randint
from time import sleep
from game import *

NUMBER_WINNER = randint(1,100)

player_name = ask_name()

round_number = 1
winner = False

gretting(player_name)

while winner == False:
    print(f'--Round {round_number}--')

    ask_gess(player_name)
    player_guess = save_gess()
    player_result = qualify_guess(player_guess,NUMBER_WINNER)
    print(player_result)
    winner = is_winner(player_result)
    if winner:
        break
         
    ask_gess('Computer Player')
    computer_guess = randint(1,100)
    sleep(2)   
    print(computer_guess)
    computer_result = qualify_guess(computer_guess,NUMBER_WINNER)
    print(computer_result)
    is_winner(computer_result)

    round_number+=1
