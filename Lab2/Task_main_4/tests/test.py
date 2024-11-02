import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab2.Task_main_4.src.main import bin_search_loop
from test_utils import output_design


class InsertionSortTestCase(unittest.TestCase):
    def test_should_find(self):
        # given
        # when
        res = bin_search_loop(5, [1, 5, 8, 12, 13], [8, 1, 23, 1, 11])
        # then
        self.assertEqual(res, [2, 0, -1, 0, -1])

        # given
        # when
        res = bin_search_loop(1, [0], [0, 1])
        # then
        self.assertEqual(bin_search_loop(1, [0], [0, 1]), [0, -1])
    
    def test_should_fit_time_memory_limit(self):
        # given
        minimum_inp = [0]
        # when
        # then
        output_design(1, bin_search_loop, 1, minimum_inp, [0])
        
        # given
        medium_inp = list(range(10**3))
        # when
        # then
        output_design(2, bin_search_loop, 10**3, medium_inp, list(range(10**3)))

        # given
        maximum_inp = list(range(10**5))
        # when
        # then
        output_design(3, bin_search_loop, 10**5, maximum_inp, [0]*10**5)


if __name__ == "__main__":
    unittest.main()