import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab2.Task_main_4.src.main import bin_search_loop
from test_utils import (
    ConsoleTimeMemory as TM, 
    get_task_name,
    MB
)


class TestCaseInsertionSort(unittest.TestCase):
    def test_should_find(self):
        # given
        inp = [1, 5, 8, 12, 13], [8, 1, 23, 1, 11]
        expected_res = [2, 0, -1, 0, -1]
        # when
        res = bin_search_loop(len(inp[0]), *inp)
        # then
        self.assertEqual(res, expected_res)

    def test_should_find_in_len_1(self):
        # given
        inp = [0], [0, 1]
        expected_res = [0, -1]
        # when
        res = bin_search_loop(len(inp[0]), *inp)
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
        test_data = [(f'{i} элементов', (i, list(range(i)), [0]*i)) for i in 
                     (10, 1000, 10**5)]

        
        print()
        print('-'*55)
        print(get_task_name(PATH))

        for test_name, input_by_size in test_data:
            # when
            res_time = TM.count_time(bin_search_loop, *input_by_size)
            res_memory = TM.count_memory(bin_search_loop, *input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)

        print('-'*55)


if __name__ == "__main__":
    unittest.main()