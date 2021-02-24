import unittest
from fizzbuzz_checker import fizzbuzzChecker

class BisextileTest(unittest.TestCase):

    def test_should_not_be_null(self):
        actual = fizzbuzzChecker.is_bob(0)
        self.assertFalse(actual, "Should be false")