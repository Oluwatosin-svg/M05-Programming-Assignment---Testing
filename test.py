import unittest

from my_sum import sum
from fractions import Fraction


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)   

if __name__ == '__main__':
    unittest.main()

#The test result of the code displays that 1 test was run
#The indicate that the code is working and no error has occured.
#The last input in the code will also help in produce the test result.

#After defining the fraction to the code, the test result showed that the
#one of the test failed. It also indicates that 2 tests was ran and only one failed
#This means that one failed and one passed.