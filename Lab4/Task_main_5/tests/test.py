import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab4.Task_main_5.src.main import solution
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestsMaxStack(unittest.TestCase):
    def test_should_find_max(self):
        # given
        inp = [
        'push 2',
        'push 3',
        'push 9',
        'push 7',
        'push 2',
        'max',
        'max',
        'max',
        'pop',
        'max']
        # when
        # then
        self.assertEqual(solution(inp), [9, 9, 9, 9])

        # given
        inp = ['push 7',
               'push 1',
               'push 7',
               'max',
               'pop',
               'max']
        # when
        # then
        self.assertEqual(solution(inp), [7, 7])

        # given
        inp = ['push 1',
               'push 2',
               'max',
               'pop',
               'max']
        # when
        # then
        self.assertEqual(solution(inp), [2, 1])

        # given
        inp = ['push 2',
               'push 1',
               'max',
               'pop',
               'max']
        # when
        # then
        self.assertEqual(solution(inp), [2, 2])
    
    def test_should_fit_time_memory_limit(self):
        test_data = [('100 элементов', [f'push {i}' for i in range(50)] + ['max', 'pop']*25),
                     ('10e4 элементов', [f'push {i}' for i in range(5*10**3)] + ['max', 'pop']*25*10**2),
                     ('4*10e5 элементов', [f'push {i}' for i in range(2*10**5)] + ['max', 'pop']*10**5)]

        expected_memory = 512 * MB
        expected_time = 5

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