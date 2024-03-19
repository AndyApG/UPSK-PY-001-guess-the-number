# -*- coding: latin-1 -*-
from time import sleep
from game import *

if __name__ == '__main__':
    game = Game()
    game.ask_name()

    player = Player(game.players[1])
    computer = Computer(game.players[0])

    while(game.winner == ""):

        game.play_turn(player.name)
        player.make_guess()
        game.check_guess(player.guess,player.name)
        print(game.result)
         
        if(game.result == "you winn!"):
            print(player.guesses[1:])
            res = input("Play again? y/n :")
            if(res == "y"):
                player = Player(game.players[1])
                computer = Computer(game.players[0])
                game = Game()
                
            else:
                break
        else:
            game.play_turn(computer.name)
            computer.make_guess(computer.guesses[-1],player.guesses[-1])
            print(computer.guess)
            game.check_guess(computer.guess,computer.name)
            print(game.result)

            if(game.result == "you winn!"):
                print(computer.guesses[1:])
                res = input("Play again? y/n :")
                if(res == "y"):
                    player = Player(game.players[1])
                    computer = Computer(game.players[0])
                    game = Game()
                else:
                    break

