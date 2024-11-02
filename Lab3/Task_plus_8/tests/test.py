import unittest
import sys
import os
from random import randint

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab3.Task_plus_8.src.main import solution
from test_utils import output_design


class PointsTestCase(unittest.TestCase):
    def test_should_find_k_nearest_points(self):
        # given
        inp = [[3, 3], [-2, 4], [5, -1]]
        # when
        # then
        self.assertEqual(solution(3, 2, inp), [[3, 3], [-2, 4]])
        
        # given
        inp = [[1,3], [-2,2]]
        # when
        # then
        self.assertEqual(solution(2, 1, inp), [[-2,2]])

        # given
        inp = [[3, 3], [-2, 4], [5, -1]]
        # when
        # then
        self.assertEqual(solution(3, 0, inp), [])
    
    def test_should_fit_time_memory_limit(self):
        # given
        minimum_inp = [[0, i] for i in range(10)]
        # when
        # then
        output_design('10 элементов', solution, 10, 10, minimum_inp)

        # given
        medium_inp = [[randint(-100, 100), randint(-100, 100)] for _ in range(10000)]
        # when
        # then
        output_design('10000 элементов', solution, 10000, 10000, medium_inp)

        # given
        maximum_inp = [[randint(-10**4, 10**4), randint(-10**4, 10**4)] for _ in range(10**5)]
        # when
        # then
        output_design('10e5 элементов', solution, 10**5, 10**5, maximum_inp)


if __name__ == "__main__":
    unittest.main()