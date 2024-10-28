import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab2.Task_main_6.src.main import solution, diff_array
from test_utils import output_design


class InsertionSortTestCase(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(diff_array(17, [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]), 
                         [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])
        self.assertEqual(solution(17, [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]),
                          (7, 11, 43))
    
    def test_time_memory(self):
        output_design(1, solution, 2, [0, 1])

        output_design(2, solution, 10**3, list(range(10**3)))

        output_design(3, solution, 10**4, list(range(10**4)))


if __name__ == "__main__":
    unittest.main()