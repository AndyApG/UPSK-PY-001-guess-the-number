from random import randint
      
class Game:
    name_player = input('What is your name? ',)
    
    def __init__(self):
        self.number_winner = randint(1,100)
        self.turn = 0
        self.name_winner = None
        self.guesses_winner = []
        self.players = ["Computer",self.name_player]
    
    
    def play_turn(self):
        self.turn += 1
        
        if(self.turn%2 == 1):
            name = self.players[1]
        else:
            name = self.players[0]

        return name

    def check_guess(self,guess = int,player = str,guesses = list):
        if guess < self.number_winner:
            self.result = 'Too low!'
        elif guess > self.number_winner:
            self.result = 'Too high!'
        else:
            self.name_winner = player
            self.guesses_winner = guesses
            self.result = player + ' you winn!'


class Player():
    

    def __init__(self,name = str):
        self.name = name
        self.guesses = []
        

    def make_guess(self):
        try:
            self.guess = int(input(""))
        except ValueError:
            print("Your guess must be a number")
        else:
            self.guesses.append(self.guess)

    
class Computer(Player):

    def make_guess(self,a=int):
        if self.guesses.__len__() > 0:
            b = self.guesses[-1]
        else:
            b = randint(1,100)
        self.guess = (a+b)//2
        self.guesses.append(self.guess)



