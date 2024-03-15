import unittest
from unittest import mock
import io


from game import ask_name, read_gess, qualify_guess, middle_point, is_winner

class TestReadGuess(unittest.TestCase):
    
    


class TestQualifyGuess(unittest.TestCase):
    def test_lower_guess(self):
        """
        It test a lower guess 
        """
        self.assertEqual(qualify_guess(5,10),"Too low!",
                         "Should be \"Too low!\"")

    def test_higher_guess(self):
        """
        It test a higher guess
        """
        self.assertEqual(qualify_guess(20,10),"Too high!",
                         "Should be \"Too high!\"")

    def test_correct_guess(self):
        """
        It test a correct guess
        """
        self.assertEqual(qualify_guess(10,10),"you winn!",
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
        
class TestIsWinner(unittest.TestCase):
    def test_is_winner(self):
        self.assertTrue(is_winner('you winn!'),"Should be True")
        self.assertFalse(is_winner('Too low!'),"Should be False")


if __name__ == "__main__":
    unittest.main()
