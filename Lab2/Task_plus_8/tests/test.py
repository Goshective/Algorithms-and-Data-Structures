import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab2.Task_plus_8.src.main import sum_polynoms, multiply_polynoms
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestCaseMultiplyPolynomials(unittest.TestCase):
    def test_should_sum_poly(self):
        # given
        a, b = [1, 2, 3], [3, 4, 5]
        expected_res = [4, 6, 8]
        # when
        res = sum_polynoms(a, b)
        # then
        self.assertEqual(res, expected_res)

    def test_should_sum_poly_shift_1(self):
        # given
        a, b = [1, 2, 3], [3, 4, 5]
        expected_res = [3, 5, 7, 3]
        # when
        res = sum_polynoms(a, b, shift_A=1) # a0 + a1*x + ...
        # then
        self.assertEqual(res, expected_res)

    def test_should_sum_poly_shift_both(self):
        # given
        a, b = [1, 2, 3], [3, 4, 5]
        expected_res = [0, 1, 5, 7, 5]
        # when
        res = sum_polynoms(a, b, shift_A=1, shift_B=2)
        # then
        self.assertEqual(res, expected_res)

    def test_should_multiply_poly_short(self):
        # given
        a, b = [3, 2, 5], [5, 1, 2]
        expected_res = [15, 13, 33, 9, 10][::-1]
        # when
        res = multiply_polynoms(len(a), a[::-1], b[::-1])
        # then
        self.assertEqual(res, expected_res)

    def test_should_multiply_poly_long(self):
        # given
        a, b = [2, 5, 3, 1, -1], [1, 2, 2, 3, 6]
        expected_res = [2, 9, 17, 23, 34, 39, 19, 3, -6]
        # when
        res = multiply_polynoms(len(b), a, b)
        # then
        self.assertEqual(res, expected_res)
    
    def check_time_memory_limit(self, res_time, res_memory):
        # given
        expected_memory = 256 * MB
        expected_time = 2
        # when
        # then
        self.assertLessEqual(res_time, expected_time)
        self.assertLessEqual(res_memory, expected_memory)
    
    def test_should_fit_time_memory_limit(self):
        # given
        test_data = [(f'{i} элементов', (i, [1]*i, [1, -1]* (i//2))) for i in 
                     (10, 250, 500)]

        for test_name, input_by_size in test_data:
            # when
            res_time = TM.count_time(multiply_polynoms, *input_by_size)
            res_memory = TM.count_memory(multiply_polynoms, *input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)


if __name__ == "__main__":
    unittest.main()