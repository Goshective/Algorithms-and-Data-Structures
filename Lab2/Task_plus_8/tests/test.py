import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab2.Task_plus_8.src.main import sum_polynoms, multiply_polynoms
from test_utils import output_design


class InsertionSortTestCase(unittest.TestCase):
    def test_correctness_sum(self):
        self.assertEqual(sum_polynoms([1, 2, 3], [3, 4, 5]), [4, 6, 8]) 
        self.assertEqual(sum_polynoms([1, 2, 3], [3, 4, 5], shift_A=1), [3, 5, 7, 3]) # a0 + a1*x + ...
        self.assertEqual(sum_polynoms([1, 2, 3], [3, 4, 5], shift_A=1, shift_B=2), [0, 1, 5, 7, 5])

    def test_correctness_multiply(self):
        self.assertEqual(multiply_polynoms(3, [3, 2, 5][::-1], [5, 1, 2][::-1]), [15, 13, 33, 9, 10][::-1])
        self.assertEqual(multiply_polynoms(5, [2, 5, 3, 1, -1], [1, 2, 2, 3, 6]), [2, 9, 17, 23, 34, 39, 19, 3, -6])
    
    def test_time_memory(self):
        output_design(1, multiply_polynoms, 1, [0], [0])

        output_design(2, multiply_polynoms, 100, [1]* 100, [1, -1]*50)

        output_design(3, multiply_polynoms, 500, [1]* 500, [1, -1]*250)


if __name__ == "__main__":
    unittest.main()