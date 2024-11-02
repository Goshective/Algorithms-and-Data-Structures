import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab2.Task_plus_5.src.main import solution
from test_utils import output_design


class TestCaseInsertionSort(unittest.TestCase):
    def test_should_be_over_the_half(self):
        # given
        inp = [2, 3, 9, 2, 2]
        # when
        # then
        self.assertEqual(solution(len(inp), inp), 1)

        # given
        inp = [1, 2, 3, 4]
        # when
        # then
        self.assertEqual(solution(len(inp), inp), 0)

        # given
        inp = [0, 3, 9, 2, 2, 2, 2, 2, 2]
        # when
        # then
        self.assertEqual(solution(len(inp), inp), 1)

        # given
        inp = [0, 3, 0, 3, 0, 3, 0, 3, 0]
        # when
        # then
        self.assertEqual(solution(len(inp), inp), 1)

        # given
        inp = [0, 3, 0, 3, 0, 3, 0, 3, 1]
        # when
        # then
        self.assertEqual(solution(len(inp), inp), 0)
    
    def test_should_fit_time_memory_limit(self):
        # given
        minimum_inp = [1, 2, 3, 4]
        # when
        # then
        output_design(1, solution, len(minimum_inp), minimum_inp)

        # given
        medium_inp = list(range(10**3))
        # when
        # then
        output_design(2, solution, len(medium_inp), medium_inp)
        
        # given
        maximum_inp = [100]*5*10**4
        # when
        # then
        output_design(3, solution, len(maximum_inp), maximum_inp)


if __name__ == "__main__":
    unittest.main()