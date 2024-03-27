#https://docs.python.org/es/3.10/library/unittest.mock-examples.html
import unittest
from unittest.mock import patch, MagicMock
from game import Game, Player, Computer


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        mock_number_winner = MagicMock()
        mock_number_winner.return_value = 10
        self.game.number_winner = mock_number_winner()
        mock_name_player = MagicMock()
        mock_name_player.return_value = "Player"
        self.game.name_player = mock_name_player()
        mock_players = MagicMock()
        mock_players.return_value = ["Computer",self.game.name_player]
        self.game.players = mock_players()
    
    def test_name_player(self):
        self.assertEqual(self.game.name_player,'Player')
        self.assertEqual(self.game.players,["Computer","Player"])

    def test_number_winner(self):
        self.assertEqual(self.game.number_winner,10)

    def test_check_guess(self):
        self.game.check_guess(20,"Player",[])
        self.assertEqual(self.game.result,'Too high!')
        self.game.check_guess(5,"Player",[])
        self.assertEqual(self.game.result,'Too low!')
        self.game.check_guess(10,"Player",[])
        self.assertEqual(self.game.result,'Player you winn!')

    def test_play_turn(self):
        first_turn = self.game.play_turn() 
        self.assertEqual(first_turn,"Player")
        second_turn = self.game.play_turn()
        self.assertEqual(second_turn,"Computer")

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player('Player')
        mock_make_guess = MagicMock()
        mock_make_guess.return_value = 10
    
    
class TestComputer(unittest.TestCase):
    def setUp(self):
        self.computer = Computer("Computer")
                            
    def test_make_guess(self):
        self.computer.make_guess(1)
        self.assertGreaterEqual(self.computer.guess,1)
        self.assertEqual(self.computer.guesses.__len__(),1)

        
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
