import unittest
import sys
import os
from random import shuffle

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab4.Task_main_1.src.main import solution
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestsStack(unittest.TestCase):
    def test_should_emulate_stack(self):
        # given
        inp = [["+", 1],
               ['+', 10],
               ['-', None],
               ['+', 2],
               ['+', 1234],
               ['-',None]]
        # when
        # then
        self.assertEqual(solution(inp), [10, 1234])

        inp = [["+", 1],
               ['+', 10],
               ['+', 20],
               ['-', None],
               ['-', None],
               ['-',None]]
        # when
        # then
        self.assertEqual(solution(inp), [20, 10, 1])
    
    def test_should_fit_time_memory_limit(self):
        test_data = [('100 элементов', [['+', i] for i in range(5*10)] + [['-', None] for _ in range(5*10)]),
                     ('10e4 элементов', [['+', i] for i in range(5*10**3)] + [['-', None] for _ in range(5*10**3)]),
                     ('10e6 элементов', [['+', i] for i in range(5*10**5)] + [['-', None] for _ in range(5*10**5)])]

        expected_memory = 256 * MB
        expected_time = 2

        time_for_tests = []

        for time_mod, memory_mod in ((1, 0), (0, 1)):
            for test_id, (test_name, input_by_size) in enumerate(test_data):

                if time_mod:
                    time_for_tests.append(TM.count_time(solution, input_by_size))

                if memory_mod:

                    # given
                    res_memory = TM.count_memory(solution, input_by_size)
                    res_time = time_for_tests[test_id]

                    # when
                    TM.output_design(test_name, res_time, res_memory)

                    # then
                    self.assertLessEqual(res_time, expected_time)
                    self.assertLessEqual(res_memory, expected_memory)


if __name__ == "__main__":
    unittest.main()