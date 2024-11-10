import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab1.Task_main_4.src.main import linear_search
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestCaseLinearSearch(unittest.TestCase):
    def test_should_find(self):
        # given
        inp = [1, 2, 3, 4, 1, 2, 3, 1], 1
        expected_res = [0, 4, 7]
        # when
        res = linear_search(*inp)
        # then
        self.assertEqual(res, expected_res)

    def test_should_not_find(self):
        # given
        inp = [1, 2, 3, 4, 1, 2, 3, 1], 5
        expected_res = []
        # when
        res = linear_search(*inp)
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
        test_data = [(f'{i} элементов', (list(range(i)), i)) for i in 
                     (10, 100, 1000)]

        for test_name, input_by_size in test_data:
            # when
            res_time = TM.count_time(linear_search, *input_by_size)
            res_memory = TM.count_memory(linear_search, *input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)


if __name__ == "__main__":
    unittest.main()