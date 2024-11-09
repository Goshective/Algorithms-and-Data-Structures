import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab3.Task_main_2.src.main import solution
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestCaseSegments(unittest.TestCase):
    def test_shold_find__the_worst_case(self):
        # given
        inp = 3
        # when
        # then
        self.assertEqual(solution(inp), [1, 3, 2])

        # given
        inp = 4
        # when
        # then
        self.assertEqual(solution(inp), [1, 4, 2, 3])

        # given
        inp = 5
        # when
        # then
        self.assertEqual(solution(inp), [1, 4, 5, 3, 2])
        
    def check_time_memory_limit(self, res_time, res_memory):
        # given
        expected_memory = 256 * MB
        expected_time = 2
        # when
        # then
        self.assertLessEqual(res_time, expected_time)
        self.assertLessEqual(res_memory, expected_memory)
    
    def test_should_fit_time_memory_limit(self):
        test_data = (('10 элементов', 10), 
                     ('1000 элементов', 1000), 
                     ('10e6 элементов', 10**6))

        for test_name, input_by_size in test_data:
            # given
            # when
            res_time = TM.count_time(solution, input_by_size)
            res_memory = TM.count_memory(solution, input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)


if __name__ == "__main__":
    unittest.main()