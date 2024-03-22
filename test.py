from unittest import TestCase, main
from unittest.mock import patch
from game import *


class GameTest(Game):
    name_player = "Player"
    @patch('builtins.input', return_value = name_player)
    
    def __init__(self,mock_intput):
        self.number_winner = 10
        self.turn = 0
        self.name_winner = None
        self.guesses_winner = []
        self.players = ["Computer",mock_intput()]

game = GameTest()
class TestGameMethods(TestCase):
   def setUp(self):
        self.game =  GameTest()
   
    def test_players_name(self):
        
        "It test the player's name"
        self.assertEqual(game.players[1],"Player")
        self.assertEqual(game.players[0],"Computer")
    def test_lower_guess(self):
        """
        It test a lower guess 
        """
        game.check_guess(5,"Player",[])
        
        self.assertEqual(game.result,"Too low!",
                         "Should be \"Too low!\"")

    def test_higher_guess(self):
        """
        It test a higher guess
        """
        game.check_guess(20,"Player",[5])

        self.assertEqual(game.result,"Too high!",
                         "Should be \"Too high!\"")

    def test_correct_guess(self):
        """
        It test a correct guess
        """
        game.check_guess(10,"Player",[5,20,10])
        self.assertEqual(game.result,"Player you winn!",
                         "Should be \"you winn!\"")
        
      
if __name__ == "__main__":
    main()
