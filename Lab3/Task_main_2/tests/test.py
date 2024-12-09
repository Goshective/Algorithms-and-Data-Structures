import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab3.Task_main_2.src.main import solution
from test_utils import (
    ConsoleTimeMemory as TM, 
    get_task_name,
    MB
)


class TestCaseSegments(unittest.TestCase):
    def test_shold_find_the_worst_case(self):
        # given
        inp_3 = 3
        expected_res_3 = [1, 3, 2]

        inp_4 = 4
        expected_res_4 = [1, 4, 2, 3]

        inp_5 = 5
        expected_res_5 = [1, 4, 5, 3, 2]

        expected_res = [expected_res_3, 
                        expected_res_4,
                        expected_res_5]
        
        # when
        res_3 = solution(inp_3)

        res_4 = solution(inp_4)

        res_5 = solution(inp_5)

        res = [res_3, res_4, res_5]
        
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
        test_data = (('10 элементов', 10), 
                     ('1000 элементов', 1000), 
                     ('10e6 элементов', 10**6))

        
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