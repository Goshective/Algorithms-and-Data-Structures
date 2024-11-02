import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab3.Task_plus_6.src.main import (
    solution, 
    qsort,
    radix_sort,
    cross_multiplication
    )
from test_utils import output_design


class MultiArrayTestCase(unittest.TestCase):
    def test_should_sort(self):
        # given
        a, b = [7, 1, 4, 9], [2, 7, 8, 11]
        # when
        # then
        self.assertEqual(solution(4, 4, a, b, qsort), 51)
    
    def test_should_fit_time_memory_limit(self):
        for func_name, func in (('\nQuick sort (Python):', qsort), ('\nRadix sort:', radix_sort)):
            print(func_name)

            # given
            a, b = [7, 1, 4, 9], [2, 7, 8, 11]
            # when
            # then
            output_design('10 элементов', solution, 4, 4, a, b, func)

            # given
            a, b = list(range(250, 0, -1)), list(range(250, 0, -1))
            # when
            # then
            output_design('250^2 элементов', solution, 250, 250, a, b, func)
            
            # given
            a, b = list(range(1000, 0, -1)), list(range(1000, 0, -1))
            # when
            # then
            output_design('1000^2 элементов', solution, 1000, 1000, a, b, func)

    def test_should_decrease_result_by_time_of_cross_multiplication(self):
        for i in (10, 250, 1000):
            # given
            a = list(range(i))
            # when
            # then
            output_design(f'на время перемножения {i} элементов', cross_multiplication, a, a)


if __name__ == "__main__":
    unittest.main()