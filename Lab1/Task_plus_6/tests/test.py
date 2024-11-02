import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab1.Task_plus_6.src.main import bubble_sort as sort_func
from test_utils import output_design


class BubbleSortTestCase(unittest.TestCase):
    def test_should_sort(self):
        # given
        inp = [31, 41, 59, 26, 41, 58]
        # when
        sort_func(len(inp), inp)
        # then
        self.assertEqual(inp, [26, 31, 41, 41, 58, 59])

        # given
        inp = [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]
        # when
        sort_func(len(inp), inp)
        # then
        self.assertEqual(inp, list(range(10)))
    
    def test_should_fit_time_memory_limit(self):
        # given
        minimum_inp = list(range(10))
        # when
        output_design('10 элементов:', sort_func, len(minimum_inp), minimum_inp)
        # then
        self.assertEqual(minimum_inp, list(range(10)))

        # given
        maximum_inp = list(range(10**3-1, -1, -1))
        # when
        output_design('1000 элементов:', sort_func, len(maximum_inp), maximum_inp)
        # then
        self.assertEqual(maximum_inp, list(range(10**3)))
        


if __name__ == "__main__":
    unittest.main()