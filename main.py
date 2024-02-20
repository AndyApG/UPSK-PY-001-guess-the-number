# -*- coding: latin-1 -*-
from time import sleep
from game import *

NUMBER_WINNER = random(1,100)

player_name = ask_name()
player_guess_list = []
computer_guess_list = [0]
round_number = 1
winner = False



gretting(player_name)

while winner == False:
    print(f'--Round {round_number}--')
    sleep(2)  

    ask_gess(player_name)
    player_guess = read_gess()
    player_result = qualify_guess(player_guess,NUMBER_WINNER)
    sleep(2)  
    print(player_result)
    player_guess_list.append(player_guess)
    winner = is_winner(player_result)
    if winner:
        break
         
    sleep(2)  
    ask_gess('Computer Player')
    #computer_guess = random(1,100)
    #computer_guess = middle_point(computer_guess_list[-1],player_guess_list[-1]) 
    computer_guess = select_random(computer_guess_list[-1]+1,player_guess_list[-1]) 
    sleep(2) 
    print(computer_guess)
    computer_result = qualify_guess(computer_guess,NUMBER_WINNER)
    computer_guess_list.append(computer_guess)
    sleep(2) 
    print(computer_result)
    winner = is_winner(computer_result)
    if winner:
        break

    round_number+=1

print(f"{player_name}'s guess list", player_guess_list)
print("Computer's guess list", computer_guess_list[1:])