import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab2.Task_plus_7.src.main import solution
from test_utils import (
    ConsoleTimeMemory as TM, 
    get_task_name,
    MB
)


class TestCaseMaxSubarrayLinear(unittest.TestCase):
    def test_find_subarray_points(self):
        # given
        inp = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
        expected_res = (7, 11, 43)
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
                     (10, 1000, 10**4)]

        
        print()
        print('-'*55)
        print(get_task_name(PATH))

        for test_name, input_by_size in test_data:
            # when
            res_time = TM.count_time(solution, *input_by_size)
            res_memory = TM.count_memory(solution, *input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)


        print('-'*55)


if __name__ == "__main__":
    unittest.main()