import unittest
import sys
import os
from random import shuffle

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab3.Task_main_1.src.main import RandomizedQuickSort as sort_func
from test_utils import output_design


class TestsRandomizedQuickSort(unittest.TestCase):
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
        # then
        output_design('100 элементов', sort_func, minimum_inp, 0, 10**2-1)

        # given
        medium_inp = list(range(1000))
        # when
        shuffle(medium_inp)
        # then
        output_design('1000 элементов', sort_func, medium_inp, 0, 10**3-1)

        # given
        medium_inp = list(range(10**4))
        # when
        shuffle(medium_inp)
        # then
        output_design('10e4 элементов', sort_func, medium_inp, 0, 10**4-1)

        # given
        medium_inp = list(range(10**4)) * 4 # 4 copies of each element
        # when
        shuffle(medium_inp)
        # then
        output_design('4*10e4 элементов (Повторения)', sort_func, medium_inp, 0, 4*10**4-1)

        # given
        medium_inp = list(range(10**5))
        # when
        shuffle(medium_inp)
        # then
        output_design('10e5 элементов', sort_func, medium_inp, 0, 10**5-1)

        # given
        maximum_inp = [x * 100 for x in range(10**5-1, -1, -1)]
        # when
        # then
        output_design('10e5 элементов (обратно)', sort_func, maximum_inp, 0, 10**5-1)


if __name__ == "__main__":
    unittest.main()