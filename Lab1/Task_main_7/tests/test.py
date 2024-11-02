import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab1.Task_main_7.src.main import find_info
from test_utils import output_design


class TestCaseIndicesInsertionSort(unittest.TestCase):
    def test_should_find_indices(self):
        # given
        inp = [10.00, 8.70, 0.01, 5.00, 3.00]
        # when
        # then
        self.assertEqual(find_info(len(inp), inp), (3, 4, 1))

        # given
        inp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # when
        # then
        self.assertEqual(find_info(len(inp), inp), (1, 5, 9))
    
    def test_should_fit_time_memory_limit(self):
        # given
        minimum_inp = list(range(1,10))
        # when
        # then
        output_design(1, find_info, len(minimum_inp), minimum_inp)

        # given
        maximum_inp = list(range(10**3-1, 0, -1))
        # when
        # then
        output_design(2, find_info, len(maximum_inp), maximum_inp)


if __name__ == "__main__":
    unittest.main()