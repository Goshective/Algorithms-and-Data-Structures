import unittest
import sys
import os
from random import shuffle

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab3.Task_main_1.src.main import RandomizedQuickSort as sort_func
from test_utils import output_design


class RandomizedQuickSortTestCase(unittest.TestCase):
    def test_should_sort(self):
        inp = [31, 41, 59, 26, 41, 58]
        sort_func(inp, 0, len(inp) - 1)
        self.assertEqual(inp, [26, 31, 41, 41, 58, 59])

        inp = [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]
        sort_func(inp, 0, len(inp) - 1)
        self.assertEqual(inp, list(range(10)))
    
    def test_should_fit_time_memory_limit(self):
        minimum_inp = list(range(100))
        output_design('100 элементов', sort_func, minimum_inp, 0, 99)

        medium_inp = list(range(1000))
        shuffle(medium_inp)
        output_design('1000 элементов', sort_func, medium_inp, 0, 999)

        medium_inp = list(range(10**4))
        shuffle(medium_inp)
        output_design('10e4 элементов', sort_func, medium_inp, 0, 9999)

        medium_inp = list(range(10**5))
        shuffle(medium_inp)
        output_design('10e5 элементов', sort_func, medium_inp, 0, 99999)

        maximum_inp = [x * 100 for x in range(10**5-1, -1, -1)]
        output_design('10e5 элементов (обратно)', sort_func, maximum_inp, 0, 99999)


if __name__ == "__main__":
    unittest.main()