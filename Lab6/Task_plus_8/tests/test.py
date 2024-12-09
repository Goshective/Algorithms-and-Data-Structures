import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab6.Task_plus_8.src.main import solution
from test_utils import (
    ConsoleTimeMemory as TM, 
    get_task_name,
    MB
)


class TestsHashSet(unittest.TestCase):
    def test_should_iterate_through_small_values(self):
        # given
        inp = [4, 0, 0, 0, 
               1, 1, 0, 0]
        expected_res = (3, 1, 1)

        # when
        res = solution(inp)
        # then
        self.assertEqual(res, expected_res)


    def check_time_memory_limit(self, res_time, res_memory):
        # given

        expected_memory = 256 * MB
        expected_time = 5

        # when
        # then
        
        self.assertLessEqual(res_time, expected_time)
        self.assertLessEqual(res_memory, expected_memory)
    
    def test_should_fit_time_memory_limit(self):
        # given
        test_data = [('100 элементов', [100, 0, 0, 0,  1, 2, 3, 4]),
                     ('10e5 элементов', [10**5, 0, 0, 0,  123, 25345, 567, 4234]),
                     ('10e6 элементов', [10**6, 0, 0, 0,  101, 2234, 334, 445698798])]

        
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