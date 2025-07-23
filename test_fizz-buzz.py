import unittest
from fizzbuzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        # Test when a list provided
        self.assertAlmostEqual(fizz_buzz([0, 1, 2, 3]), [0, 1, 2, 'Fizz'])