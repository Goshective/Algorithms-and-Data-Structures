import unittest
import sys
import os
from random import shuffle

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab2.Task_main_1.src.main import merge_sort as sort_func
from test_utils import output_design


class InsertionSortTestCase(unittest.TestCase):
    def test_should_sort(self):
        # given
        inp = [31, 41, 59, 26, 41, 58]
        # when
        sort_func(inp, 0, len(inp) - 1)
        # then
        self.assertEqual(inp, [26, 31, 41, 41, 58, 59])

        # given
        inp = [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]
        # when
        sort_func(inp, 0, len(inp) - 1)
        # then
        self.assertEqual(inp, list(range(10)))
    
    def test_should_fit_time_memory_limit(self):
        # given
        minimum_inp = list(range(100))
        # when
        output_design('100 элементов', sort_func, minimum_inp, 0, 99)
        # then
        self.assertEqual(minimum_inp, list(range(100)))

        # given
        medium_inp = list(range(1000))
        shuffle(medium_inp)
        # when
        output_design('1000 элементов', sort_func, medium_inp, 0, 999)
        # then
        self.assertEqual(medium_inp, list(range(1000)))

        # given
        maximum_inp = [x * 5*10**4 for x in range(2*10**4-1, -1, -1)]
        # when
        output_design('2*10e4 элементов', sort_func, maximum_inp, 0, 2*10**4-1)
        # then
        self.assertEqual(maximum_inp, list(range(0, 10**9, 5*10**4)))
        


if __name__ == "__main__":
    unittest.main()