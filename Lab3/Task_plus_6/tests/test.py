import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab3.Task_plus_6.src.main import (
    solution, 
    qsort,
    radix_sort
    )
from test_utils import output_design


class MultiArrayTestCase(unittest.TestCase):
    def test_correctness(self):
        a, b = [7, 1, 4, 9], [2, 7, 8, 11]
        self.assertEqual(solution(4, 4, a, b, qsort), 51)
    
    def test_time_memory(self):
        for func_name, func in (('\nQuick sort (Python):', qsort), ('\nRadix sort:', radix_sort)):
            print(func_name)
            a, b = [7, 1, 4, 9], [2, 7, 8, 11]
            output_design('10 элементов', solution, 4, 4, a, b, func)

            a, b = list(range(100, 0, -1)), list(range(100, 0, -1))
            output_design('100^2 элементов', solution, 100, 100, a, b, func)

            a, b = list(range(1000, 0, -1)), list(range(1000, 0, -1))
            output_design('6000^2 элементов', solution, 1000, 1000, a, b, func)


if __name__ == "__main__":
    unittest.main()