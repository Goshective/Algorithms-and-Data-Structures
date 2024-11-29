import unittest
import sys
import os
from random import shuffle

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab5.Task_plus_4.src.main import solution
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestsMinHeap(unittest.TestCase):
    def test_should_work_as_basic_queue(self):
        # given
        inp = [5, 4, 3, 2, 1]
        expected_res = [(1, 4), (0, 1), (1, 3)]
        expected_size = 4*len(inp)

        # when
        res = solution(inp)
        res_size = len(res)

        # then
        self.assertEqual(res, expected_res)
        self.assertLessEqual(res_size, expected_size)

    def test_should_return_nothing(self):
        # given
        inp = [1, 2, 3, 4, 5]
        expected_res = []
        expected_size = 4*len(inp)

        # when
        res = solution(inp)
        res_size = len(res)

        # then
        self.assertEqual(res, expected_res)
        self.assertLessEqual(res_size, expected_size)

    def check_time_memory_limit(self, res_time, res_memory):
        # given
        expected_memory = 512 * MB
        expected_time = 3
        # when
        # then
        
        self.assertLessEqual(res_time, expected_time)
        self.assertLessEqual(res_memory, expected_memory)
    
    def test_should_fit_time_memory_limit(self):
        # given
        test_data = []
        for title, amount in (('100 элементов', 100), ('1000 элементов', 1000), ('10e5 элементов', 10**5)):
            lst = list(range(amount))
            shuffle(lst)
            test_data.append((title, lst))

        for test_name, input_by_size in test_data:
            # when
            res_time = TM.count_time(solution, input_by_size)
            res_memory = TM.count_memory(solution, input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)


if __name__ == "__main__":
    unittest.main()