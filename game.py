from random import randint
def read_guess():
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

def middle_point(a,b):
    return ((a + b) // 2)

class Game:
    
    def __init__(self):
        self.numberWinner = randint(1,100)
        self.winner = ""
        self.players = ["Computer"]
        print("Welcome to the guess number game")

    def ask_name(self):
        name = input('What is your name ',)
        self.players.append(name)

    def play_turn(self, player = str):
        print(f"Turn {player}, make a guess: \n")


    def check_guess(self,guess = int,player = str):
        if guess < self.numberWinner:
            self.result = 'Too low!'
        elif guess > self.numberWinner:
            self.result = 'Too high!'
        else:
            self.result = 'you winn!'
            self.winner = player


class Player:
    

    def __init__(self,name = str):
        self.name = name
        self.guesses = [0]
        

    def make_guess(self):
       self.guess = read_guess()
       self.guesses.append(self.guess)
       
    
class Computer(Player):

    def make_guess(self,a,b):
        self.guess = middle_point(a,b)
        self.guesses.append(self.guess)



