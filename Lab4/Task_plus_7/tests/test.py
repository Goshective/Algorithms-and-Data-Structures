import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab4.Task_plus_7.src.main import solution
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestsQueueMax(unittest.TestCase):
    def test_should_find_basic_max(self):
        # given
        inp = 8, [2, 7, 3, 1, 5, 2, 6, 2], 4
        expected_res = [7, 7, 5, 6, 6]

        # when
        res = solution(*inp)

        # then
        self.assertEqual(res, expected_res)

    def test_should_find_with_size_1_window(self):
        # given
        inp = 8, [2, 7, 3, 1, 5, 2, 6, 2], 1
        expected_res = [2, 7, 3, 1, 5, 2, 6, 2]

        # when
        res = solution(*inp)

        # then
        self.assertEqual(res, expected_res)

    def check_time_memory_limit(self, res_time, res_memory):
        # given
        expected_memory = 512 * MB
        expected_time = 5
        # when
        # then
        
        self.assertLessEqual(res_time, expected_time)
        self.assertLessEqual(res_memory, expected_memory)
    
    def test_should_fit_time_memory_limit(self):
        # given
        test_data = [('100 элементов', (100, list(range(100)), 50)),
                     ('1000 элементов', (1000, list(range(1000)), 500)),
                     ('10e5 элементов', (10**5, list(range(10**5)), 5*10**4))]

        for test_name, input_by_size in test_data:
            # when
            res_time = TM.count_time(solution, *input_by_size)
            res_memory = TM.count_memory(solution, *input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)


if __name__ == "__main__":
    unittest.main()