import unittest

from game import qualify_guess


class TestQualifyGess(unittest.TestCase):
    def test_lower_gess(self):
        """
        It test a lower gess 
        """
        self.assertEqual(qualify_guess(5,10),"Too low!","Should be \"Too low!\"")

    def test_higher_gess(self):
        """
        It test a higher gess
        """
        self.assertEqual(qualify_guess(20,10),"Too high!","Should be \"Too high!\"")

    def test_correct_gess(self):
        """
        It test a correct gess
        """
        self.assertEqual(qualify_guess(10,10),"you winn!","Should be \"you winn!\"")

