import unittest
from unittest import mock
import io


from game import *

class GameTest (Game):
            def __init__(self):
                self.numberWinner = 10
                self.winner = ""
                self.players = ["Computer","Player"]

game = GameTest() 

class TestQualifyGuess(unittest.TestCase):
   

    def test_lower_guess(self):
        """
        It test a lower guess 
        """
        game.check_guess(5,"Player")
        
        self.assertEqual(game.result,"Too low!",
                         "Should be \"Too low!\"")

    def test_higher_guess(self):
        """
        It test a higher guess
        """
        game.check_guess(20,"Player")

        self.assertEqual(game.result,"Too high!",
                         "Should be \"Too high!\"")

    def test_correct_guess(self):
        """
        It test a correct guess
        """
        game.check_guess(10,"Player")
        self.assertEqual(game.result,"you winn!",
                         "Should be \"you winn!\"")
        
    

class TestMiddlePoint(unittest.TestCase):
    def test_a_b(self):
        """
        It test if the middle point is correct 
        """
        self.assertEqual(middle_point(0,10),5,
                          "Should be 5")
        self.assertEqual(middle_point(10,1),5,
                          "Should be 5")
        self.assertEqual(middle_point(-1,10),4,
                          "Should be 4")
        


if __name__ == "__main__":
    unittest.main()
