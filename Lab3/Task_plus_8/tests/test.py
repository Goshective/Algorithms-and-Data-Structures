import unittest
import sys
import os
from random import randint

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab3.Task_plus_8.src.main import solution
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestCasePoints(unittest.TestCase):
    def test_should_find_k_nearest_points(self):
        # given
        inp = [[3, 3], [-2, 4], [5, -1]]
        excepted_res = [[3, 3], [-2, 4]]
        # when
        res = solution(3, 2, inp)
        # then
        self.assertEqual(res, excepted_res)
        
    def test_should_return_nothing(self):
        # given
        inp = [[3, 3], [-2, 4], [5, -1]]
        # when
        # then
        self.assertEqual(solution(3, 0, inp), [])
    
    def check_time_memory_limit(self, res_time, res_memory):
        # given
        expected_memory = 256 * MB
        expected_time = 2
        # when
        # then
        self.assertLessEqual(res_time, expected_time)
        self.assertLessEqual(res_memory, expected_memory)
    
    def test_should_fit_time_memory_limit(self):
        minimum_inp = [[0, i] for i in range(10)]
        medium_inp = [[randint(-100, 100), randint(-100, 100)] for _ in range(10000)]
        maximum_inp = [[randint(-10**4, 10**4), randint(-10**4, 10**4)] for _ in range(10**5)]

        test_data = [('10 элементов', (10, 10, minimum_inp)),
                     ('10000 элементов', (10000, 10000, medium_inp)),
                     ('10e5 элементов', (10**5, 10**5, maximum_inp))]

        for test_name, input_by_size in test_data:
            # given
            # when
            res_time = TM.count_time(solution, *input_by_size)
            res_memory = TM.count_memory(solution, *input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)
                    

if __name__ == "__main__":
    unittest.main()