import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab2.Task_plus_8.src.main import sum_polynoms, multiply_polynoms
from test_utils import output_design


class TestCaseMultiplyPolynomials(unittest.TestCase):
    def test_should_sum_poly(self):
        # given
        a, b = [1, 2, 3], [3, 4, 5]
        # when
        # then
        self.assertEqual(sum_polynoms(a, b), [4, 6, 8]) 

        # given
        a, b = [1, 2, 3], [3, 4, 5]
        # when
        # then
        self.assertEqual(sum_polynoms(a, b, shift_A=1), [3, 5, 7, 3]) # a0 + a1*x + ...

        # given
        a, b = [1, 2, 3], [3, 4, 5]
        # when
        # then
        self.assertEqual(sum_polynoms(a, b, shift_A=1, shift_B=2), [0, 1, 5, 7, 5])

    def test_should_multiply_poly(self):
        # given
        a, b = [3, 2, 5], [5, 1, 2]
        # when
        # then
        self.assertEqual(multiply_polynoms(len(a), a[::-1], b[::-1]), [15, 13, 33, 9, 10][::-1])

        # given
        a, b = [2, 5, 3, 1, -1], [1, 2, 2, 3, 6]
        # when
        # then
        self.assertEqual(multiply_polynoms(len(b), a, b), [2, 9, 17, 23, 34, 39, 19, 3, -6])
    
    def test_should_fit_time_memory_limit(self):
        # given
        minimum_inp = [0]
        # when
        # then
        output_design(1, multiply_polynoms, 1, minimum_inp, minimum_inp)

        # given
        medium_inp = [1]* 100, [1, -1]*50
        # when
        # then
        output_design(2, multiply_polynoms, 100, *medium_inp)

        # given
        maximum_inp = [1]* 500, [1, -1]*250
        # when
        # then
        output_design(3, multiply_polynoms, 500, *maximum_inp)


if __name__ == "__main__":
    unittest.main()