import unittest
from fizzbuzz_checker import fizzbuzzChecker

class BisextileTest(unittest.TestCase):

    def test_should_be_zero(self):
        actual = fizzbuzzChecker.is_bob(1)
        self.assertFalse(actual, "zéro")

    def test_should_be_negative(self):
        actual = fizzbuzzChecker.is_bob(1)
        self.assertFalse(actual, "négatif")

    def test_should_be_multiple_three(self):
        actual = fizzbuzzChecker.is_bob(4)
        self.assertFalse(actual, "Fizz")

    def test_should_be_multiple_five(self):
        actual = fizzbuzzChecker.is_bob(8)
        self.assertFalse(actual, "Fizz")
