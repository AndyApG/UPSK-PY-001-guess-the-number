from random import randint
def ask_name():
    return input('What is your first name ',)
    
def gretting(name):
   print(f'{name}, welcome to the guess number game we going to satart ...')

def ask_gess(player):
    print(f'{player}, enter your guess: ')

def read_gess():
    return(int(input()))

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



