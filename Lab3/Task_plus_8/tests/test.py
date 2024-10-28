import unittest
import sys
import os
from random import randint

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab3.Task_plus_8.src.main import solution
from test_utils import output_design


class PointsTestCase(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(solution(3, 2, [[3, 3], [-2, 4], [5, -1]]), [[3, 3], [-2, 4]])

        self.assertEqual(solution(2, 1, [[1,3], [-2,2]]), [[-2,2]])

        self.assertEqual(solution(3, 0, [[3, 3], [-2, 4], [5, -1]]), [])
    
    def test_time_memory(self):
        output_design('10 элементов', solution, 10, 10, [[0, i] for i in range(10)])

        medium_inp = [[randint(-100, 100), randint(-100, 100)] for _ in range(1000)]
        output_design('1000 элементов', solution, 1000, 1000, medium_inp)

        maximum_inp = [[randint(-10**4, 10**4), randint(-10**4, 10**4)] for _ in range(10**5)]
        output_design('5000 элементов', solution, 10**5, 10**5, maximum_inp)


if __name__ == "__main__":
    unittest.main()