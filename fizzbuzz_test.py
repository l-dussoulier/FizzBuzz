import unittest
from fizzbuzz_checker import fizzbuzzChecker

class BisextileTest(unittest.TestCase):

    def test_should_not_be_zero(self):
        actual = fizzbuzzChecker.is_bob(1)
        self.assertFalse(actual, "Should be false")
