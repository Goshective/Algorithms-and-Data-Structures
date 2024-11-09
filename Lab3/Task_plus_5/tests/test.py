import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab3.Task_plus_5.src.main import solution
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestCaseHirschIndex(unittest.TestCase):
    def test_find_hirsch_index(self):
        # given
        inp = [3,0,6,1,5]
        expected_res = 3
        # when
        res = solution(inp)
        # then
        self.assertEqual(res, expected_res)

    def test_should_find_minimum(self):
        # given
        inp = [1,3,1]
        expected_res = 1
        # when
        res = solution(inp)
        # then
        self.assertEqual(res, expected_res)

    def test_should_find_maximum(self):
        # given
        inp = [500,500,600]
        expected_res = 3
        # when
        res = solution(inp)
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
        minimum_inp = list(range(10))
        medium_inp = [100 - i for i in range(100)]
        maximum_inp = [(5000 - i) // 5 for i in range(5000)]

        test_data = [('10 элементов', minimum_inp),
                     ('100 элементов', medium_inp),
                     ('5000 элементов', maximum_inp)]

        for test_name, input_by_size in test_data:
            # when
            res_time = TM.count_time(solution, input_by_size)
            res_memory = TM.count_memory(solution, input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)


if __name__ == "__main__":
    unittest.main()