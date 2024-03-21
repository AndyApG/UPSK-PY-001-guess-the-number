from random import randint
      

def middle_point(a,b):
    return ((a + b) // 2)

class Game:
    
    def __init__(self):
        self.numberWinner = randint(1,100)
        self.round = 0
        self.winner = None
        self.players = ["Computer","Player"]

    def ask_name(self):
        name = input('What is your name ',)
        self.players[1] = name

    def play_turn(self):
        self.round += 1
        
        if(self.round%2 == 1):
            name = self.players[1]
        else:
            name = self.players[0]

        return name

    def isguess_valid(self, number = int):

        if 0 >= number or number > 100:
            return True
        else:
            return False


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
        self.guesses = []
        

    def make_guess(self):
       self.guess = int(input(""))
       self.guesses.append(self.guess)
       
    
class Computer(Player):

    def make_guess(self,a,b):
        self.guess = middle_point(a,b)
        self.guesses.append(self.guess)



