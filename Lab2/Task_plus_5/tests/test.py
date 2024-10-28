import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab2.Task_plus_5.src.main import solution
from test_utils import output_design


class InsertionSortTestCase(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(solution(5, [2, 3, 9, 2, 2]), 1)
        self.assertEqual(solution(4, [1, 2, 3, 4]), 0)
        self.assertEqual(solution(9, [0, 3, 9, 2, 2, 2, 2, 2, 2]), 1)
        self.assertEqual(solution(9, [0, 3, 0, 3, 0, 3, 0, 3, 0]), 1)
        self.assertEqual(solution(9, [0, 3, 0, 3, 0, 3, 0, 3, 1]), 0)
    
    def test_time_memory(self):
        output_design(1, solution, 4, [1, 2, 3, 4])

        output_design(2, solution, 10**3, list(range(10**3)))

        output_design(3, solution, 5*10**4, [100]*5*10**4)


if __name__ == "__main__":
    unittest.main()