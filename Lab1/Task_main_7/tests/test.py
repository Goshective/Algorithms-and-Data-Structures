import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab1.Task_main_7.src.main import find_info
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestCaseIndicesInsertionSort(unittest.TestCase):
    def test_should_find_indices_float(self):
        # given
        inp = [10.00, 8.70, 0.01, 5.00, 3.00]
        expected_res = (3, 4, 1)
        # when
        res = find_info(len(inp), inp)
        # then
        self.assertEqual(res, expected_res)

    def test_should_find_indices_sorted(self):
        # given
        inp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_res = (1, 5, 9)
        # when
        res = find_info(len(inp), inp)
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
        test_data = [(f'{i} элементов', (i, list(range(i, -1, -1)))) for i in 
                     (10, 100, 1000)]

        for test_name, input_by_size in test_data:
            # when
            res_time = TM.count_time(find_info, *input_by_size)
            res_memory = TM.count_memory(find_info, *input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)


if __name__ == "__main__":
    unittest.main()