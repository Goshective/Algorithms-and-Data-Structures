import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab7.Task_plus_2.src.main import solution
from test_utils import (
    ConsoleTimeMemory as TM, 
    get_task_name,
    MB
)


class TestsHashTable(unittest.TestCase):
    def test_should_solve_minimum(self):
        # given
        inp = 1
        expected_res = [1]

        # when
        res = solution(inp)

        # then
        self.assertEqual(res, expected_res)

    def test_should_solve_small_number(self):
        # given
        inp = 5
        expected_res = [1, 2, 4, 5]

        # when
        res = solution(inp)

        # then
        self.assertEqual(res, expected_res)

    def test_should_solve_by_multiple_divisions(self):
        # given
        inp = 96234
        expected_res = [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234]

        # when
        res = solution(inp)

        # then
        self.assertEqual(res, expected_res)

    def check_time_memory_limit(self, res_time, res_memory):
        # given

        expected_memory = 256 * MB
        expected_time = 1

        # when
        # then
        
        self.assertLessEqual(res_time, expected_time)
        self.assertLessEqual(res_memory, expected_memory)
    
    def test_should_fit_time_memory_limit(self):
        # given
        test_data = []
        for title, n in (('100 элементов', 100), ('10e4 элементов', 1000), ('10e6 элементов', 10**5)):
            test_data.append((title, n))

        
        print()
        print('-'*55)
        print(get_task_name(PATH))

        for test_name, input_by_size in test_data:
            # when
            res_time = TM.count_time(solution, input_by_size)
            res_memory = TM.count_memory(solution, input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)

        print('-'*55)


if __name__ == "__main__":
    unittest.main()