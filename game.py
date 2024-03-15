from random import randint
import os

def ask_name():
    return input('What is your first name ',)
    
def gretting(name):
   print(f'{name}, welcome to the guess number game we going to satart ...')

def ask_guess(player):
    print(f'{player}, enter your guess: ')

def read_gess():
    while True:
        try:
            number = int(input(""))
        except ValueError:
            print("Write a number")
            continue

        if 0 >= number or number > 100:
            print("Your guess must be between 1 and 100")
            continue
        else:
            return number
    

def qualify_guess(guess, number):
    if guess < number:
        return('Too low!')
    elif guess > number:
        return('Too high!')
    else:
        return('you winn!')
    
def is_winner(result):
    if result == 'you winn!':
        return True
    else: 
        return False
    
def random(min,max):
    return randint(min,max)

def middle_point(a,b):
    return ((a + b) // 2)

def select_random(a,b):
    if a < b:
        return random(a,b)
    elif b < a:
        return random(b,a)
    else:
        return b + 1
    
def new_game(play):
    if play == 'Y' or play == "yes" or play == "Yes" or play == "S" or play == "si":
        os.system('python main.py')
    else:
        print("Tanks!")



