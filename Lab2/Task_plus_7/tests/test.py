import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab2.Task_plus_7.src.main import solution
from test_utils import output_design


class MaxSubarrayLinearTestCase(unittest.TestCase):
    def test_find_subarray_points(self):
        # given
        arr = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
        # when
        # then
        self.assertEqual(solution(len(arr), arr),
                          (7, 11, 43))
    
    def test_should_fit_time_memory_limit(self):
        # given
        minimum_inp = [0, 1]
        # when
        # then
        output_design(1, solution, len(minimum_inp), minimum_inp)

        # given
        medium_inp = list(range(10**3))
        # when
        # then
        output_design(2, solution, len(medium_inp), medium_inp)

        # given
        maximum_inp = list(range(10**4))
        # when
        # then
        output_design(3, solution, len(maximum_inp), maximum_inp)


if __name__ == "__main__":
    unittest.main()