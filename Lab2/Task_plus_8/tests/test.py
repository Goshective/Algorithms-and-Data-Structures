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
        test_data = [(f'{i} элементов', (i, [1]*i, [1, -1]* (i//2))) for i in 
                     (10, 250, 500)]

        expected_memory = 256 * MB
        expected_time = 2

        time_for_tests = []

        for time_mod, memory_mod in ((1, 0), (0, 1)):
            for test_id, (test_name, input_by_size) in enumerate(test_data):

                if time_mod:
                    time_for_tests.append(TM.count_time(multiply_polynoms, *input_by_size))

                if memory_mod:

                    # given
                    res_memory = TM.count_memory(multiply_polynoms, *input_by_size)
                    res_time = time_for_tests[test_id]

                    # when
                    TM.output_design(test_name, res_time, res_memory)

                    # then
                    self.assertLessEqual(res_time, expected_time)
                    self.assertLessEqual(res_memory, expected_memory)


if __name__ == "__main__":
    unittest.main()