import unittest
import sys
import os
from random import shuffle

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab2.Task_main_1.src.main import merge_sort
from test_utils import output_design


class InsertionSortTestCase(unittest.TestCase):
    def test_correctness(self):
        inp = [31, 41, 59, 26, 41, 58]
        merge_sort(inp, 0, len(inp) - 1)
        self.assertEqual(inp, [26, 31, 41, 41, 58, 59])

        inp = [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]
        merge_sort(inp, 0, len(inp) - 1)
        self.assertEqual(inp, list(range(10)))
    
    def test_time_memory(self):
        minimum_inp = list(range(100))
        output_design('100 элементов', merge_sort, minimum_inp, 0, 99)
        self.assertEqual(minimum_inp, list(range(100)))

        medium_inp = list(range(1000))
        shuffle(medium_inp)
        output_design('1000 элементов', merge_sort, medium_inp, 0, 999)
        self.assertEqual(medium_inp, list(range(1000)))

        maximum_inp = [x * 5*10**4 for x in range(2*10**4-1, -1, -1)]
        output_design('2*10e4 элементов', merge_sort, maximum_inp, 0, 2*10**4-1)
        self.assertEqual(maximum_inp, list(range(0, 10**9, 5*10**4)))
        


if __name__ == "__main__":
    unittest.main()