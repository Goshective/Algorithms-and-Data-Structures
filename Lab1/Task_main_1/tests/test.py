import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab1.Task_main_1.src.main import insertion_sort as sort_func
from test_utils import (
    ConsoleTimeMemory as TM, 
    get_task_name,
    MB
)


class TestCaseInsertionSort(unittest.TestCase):
    def test_should_sort_example(self):
        # given
        inp = [31, 41, 59, 26, 41, 58]
        expected_res = [26, 31, 41, 41, 58, 59]
        # when
        sort_func(len(inp), inp)
        res = inp
        # then
        self.assertEqual(res, expected_res)

    def test_should_sort_growing_sequence(self):
        # given
        inp = [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]
        expected_res = list(range(10))
        # when
        sort_func(len(inp), inp)
        res = inp
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
        test_data = [(f'{i} элементов', (i, list(range(i, 0, -1)))) for i in 
                     (10, 100, 1000)]

        
        print()
        print('-'*55)
        print(get_task_name(PATH))

        for test_name, input_by_size in test_data:
            # when
            res_time = TM.count_time(sort_func, *input_by_size)
            res_memory = TM.count_memory(sort_func, *input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)
        

        print('-'*55)


if __name__ == "__main__":
    unittest.main()