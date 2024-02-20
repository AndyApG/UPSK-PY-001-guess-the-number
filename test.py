import unittest

from game import qualify_guess, middle_point


class TestQualifyGess(unittest.TestCase):
    def test_lower_gess(self):
        """
        It test a lower gess 
        """
        self.assertEqual(qualify_guess(5,10),"Too low!",
                         "Should be \"Too low!\"")

    def test_higher_gess(self):
        """
        It test a higher gess
        """
        self.assertEqual(qualify_guess(20,10),"Too high!",
                         "Should be \"Too high!\"")

    def test_correct_gess(self):
        """
        It test a correct gess
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
        


