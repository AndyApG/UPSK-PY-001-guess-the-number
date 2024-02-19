# -*- coding: latin-1 -*-
from random import randint

NUMBER_WINNER = randint(1,100)

player_name = input('What is your name ',)

round_number = 1
winner = False

print(f'{player_name}, welcome to the guess number game we going to satart ...')

while winner == False:
    print(f'--Round {round_number}--')

    player_guess = int(input(f'{player_name}, enter your guess: '))

    if player_guess < NUMBER_WINNER:
        print('Too low!')
    elif player_guess > NUMBER_WINNER:
        print('Too high!')
    else:
        print(f'{player_name} you are the winner!')
        winner = True
        break

    computer_guess = randint(1,100)
    print(f'Computer player, enter your gess: {computer_guess}')

    if computer_guess < NUMBER_WINNER:
        print('Too low!')
    elif computer_guess > NUMBER_WINNER:
        print('Too high!')
    else:
        print('Computer player is the winner!')
        winner = True
        break

    round_number+=1





