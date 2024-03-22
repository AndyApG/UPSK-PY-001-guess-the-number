# -*- coding: latin-1 -*-
from game import *

def main():
    print("Guess the number between 1 and 100. Good luck!")
    
    game = Game()
    player = Player(game.players[1])
    computer = Computer(game.players[0])

    while(game.name_winner == None):

        print(f"\n{game.play_turn()} make a guess:")
        if(game.turn%2 == 1):
            while True:
                try:
                    player.make_guess()
                    game.check_guess(player.guess,player.name,player.guesses)
                except AttributeError:
                    print("try again")
                else:
                    print(game.result)
                    break
           
        else:
            computer.make_guess(player.guesses[-1]) 
            print(computer.guess)   
            game.check_guess(computer.guess,computer.name,computer.guesses)
            print(game.result)

         
        if(game.name_winner != None):
            print(game.guesses_winner)
            res = input("Play again? y/n :")

            if(res == "y"):
                main()   
            else:
                break



if __name__ == '__main__':
    main()