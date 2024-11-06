import unittest
import sys
import os
from random import shuffle

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab4.Task_main_4.src.main import solution
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestsBrackets(unittest.TestCase):
    def test_should_find_wrong_index(self):
        # given
        inp = '[]'
        # when
        # then
        self.assertEqual(solution(inp), 'Success')

        inp = '{}[]'
        # when
        # then
        self.assertEqual(solution(inp), 'Success')

        inp = '[()]'
        # when
        # then
        self.assertEqual(solution(inp), 'Success')

        inp = '{'
        # when
        # then
        self.assertEqual(solution(inp), 1)

        inp = '{[}'
        # when
        # then
        self.assertEqual(solution(inp), 3)

        inp = 'foo(bar);'
        # when
        # then
        self.assertEqual(solution(inp), 'Success')

        inp = 'foo(bar[i);'
        # when
        # then
        self.assertEqual(solution(inp), 10)
    
    def test_should_fit_time_memory_limit(self):
        test_data = [('100 элементов', '('*5*10 + ')'*5*10),
                     ('10e4 элементов', '('*5*10**3 + ')'*5*10**3),
                     ('10e6 элементов', '('*5*10**5 + ')'*5*10**5)]

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