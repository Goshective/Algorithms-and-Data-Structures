import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab1.Task_plus_9.src.main import bin_sum
from test_utils import output_design


class TestCaseInsertionSort(unittest.TestCase):
    def test_should_sum(self):
        # given
        a, b = list(map(int, '1000001')), list(map(int, '1111111'))
        # when
        # then
        self.assertEqual(bin_sum(a, b), list(map(int, '11000000')))
        
        # given
        a, b = [0], [0]
        # when
        # then
        self.assertEqual(bin_sum(a, b), [0])

        # given
        a, b = [0], [1]
        # when
        # then
        self.assertEqual(bin_sum(a, b), [1])

        # given
        a, b = [a, b]
        # when
        # then
        self.assertEqual(bin_sum(a, b), [1])

        # given
        a, b = [1], [1]
        # when
        # then
        self.assertEqual(bin_sum(a, b), [1, 0])
    
    def test_should_fit_time_memory_limit(self):
        # given
        minimum_inp = [1], [0]
        # when
        # then
        output_design(1, bin_sum, *minimum_inp)

        # given
        maximum_inp = [1]*10**3, [1]*10**3
        # when
        # then
        output_design(2, bin_sum, *maximum_inp)


if __name__ == "__main__":
    unittest.main()