import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab2.Task_plus_5.src.main import solution
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestCaseInsertionSort(unittest.TestCase):
    def test_should_be_over_the_half(self):
        # given
        inp = [2, 3, 9, 2, 2]
        expected_res = 1
        # when
        res = solution(len(inp), inp)
        # then
        self.assertEqual(res, expected_res)

    def test_should_be_over_the_half_different(self):
        # given
        inp = [1, 2, 3, 4]
        expected_res = 0
        # when
        res = solution(len(inp), inp)
        # then
        self.assertEqual(res, expected_res)

    def test_should_be_over_the_half_by_one(self):
        # given
        inp = [0, 3, 0, 3, 0, 3, 0, 3, 0]
        expected_res = 1
        # when
        res = solution(len(inp), inp)
        # then
        self.assertEqual(res, expected_res)

    def test_should_be_over_the_half_equal(self):
        # given
        inp = [0, 3, 0, 3, 0, 3, 0, 3, 1]
        expected_res = 0
        # when
        res = solution(len(inp), inp)
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
        test_data = [(f'{i} элементов', (i, list(range(i)))) for i in 
                     (10, 1000, 10**5)]

        for test_name, input_by_size in test_data:
            # when
            res_time = TM.count_time(solution, *input_by_size)
            res_memory = TM.count_memory(solution, *input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)


if __name__ == "__main__":
    unittest.main()