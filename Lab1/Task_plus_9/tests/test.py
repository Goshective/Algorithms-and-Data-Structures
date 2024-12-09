import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab1.Task_plus_9.src.main import bin_sum
from test_utils import (
    ConsoleTimeMemory as TM, 
    get_task_name,
    MB
)


class TestCaseInsertionSort(unittest.TestCase):
    def test_should_sum_long(self):
        # given
        a, b = list(map(int, '1000001')), list(map(int, '1111111'))
        expected_res = list(map(int, '11000000'))
        # when
        res = bin_sum(a, b)
        # then
        self.assertEqual(res, expected_res)

    def test_shold_sum_zero(self): 
        # given
        a, b = [0], [0]
        expected_res = [0]
        # when
        res = bin_sum(a, b)
        # then
        self.assertEqual(res, expected_res)
    def test_shold_sum_with_digit_transition(self):
        # given
        a, b = [1], [1]
        expected_res = [1, 0]
        # when
        res = bin_sum(a, b)
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
        test_data = [(f'{i} элементов', ([1]*i, [1]*i)) for i in 
                     (10, 100, 1000)]

        
        print()
        print('-'*55)
        print(get_task_name(PATH))

        for test_name, input_by_size in test_data:
            # when
            res_time = TM.count_time(bin_sum, *input_by_size)
            res_memory = TM.count_memory(bin_sum, *input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)

        print('-'*55)


if __name__ == "__main__":
    unittest.main()