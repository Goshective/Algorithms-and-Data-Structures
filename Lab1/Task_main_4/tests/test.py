import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab1.Task_main_4.src.main import linear_search
from test_utils import output_design


class LinearSearchTestCase(unittest.TestCase):
    def test_should_search(self):
        # given
        inp = [1, 2, 3, 4, 1, 2, 3, 1], 1
        # when
        # then
        self.assertEqual(linear_search(*inp), [0, 4, 7])

        # given
        inp = [1, 2, 3, 4, 1, 2, 3, 1], 5
        # when
        # then
        self.assertEqual(linear_search(*inp), [])
    
    def test_should_fit_time_memory_limit(self):
        # given
        minimum_inp = list(range(10))
        # when
        # then
        output_design(1, linear_search, minimum_inp, 4)

        # given
        maximum_inp = list(range(10**3))
        # when
        # then
        output_design(2, linear_search, maximum_inp, 10**3)


if __name__ == "__main__":
    unittest.main()