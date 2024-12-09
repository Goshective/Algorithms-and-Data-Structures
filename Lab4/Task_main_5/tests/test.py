import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab4.Task_main_5.src.main import solution
from test_utils import (
    ConsoleTimeMemory as TM, 
    get_task_name,
    MB
)


class TestsMaxStack(unittest.TestCase):
    def test_should_find_constant_max(self):
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
        expected_res = [9, 9, 9, 9]

        # when
        res = solution(inp)

        # then
        self.assertEqual(res, expected_res)

    def test_should_find_max_after_pop(self):
        # given
        inp = ['push 5',
               'push 1',
               'push 7',
               'max',
               'pop',
               'max']
        expected_res = [7, 5]

        # when
        res = solution(inp)

        # then
        self.assertEqual(res, expected_res)

    def test_should_find_constant_max_after_pop(self):
        # given
        inp = ['push 2',
               'push 1',
               'max',
               'pop',
               'max']
        expected_res = [2, 2]

        # when
        res = solution(inp)

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
        test_data = [('100 элементов', [f'push {i}' for i in range(50)] + ['max', 'pop']*25),
                     ('10e4 элементов', [f'push {i}' for i in range(5*10**3)] + ['max', 'pop']*25*10**2),
                     ('4*10e5 элементов', [f'push {i}' for i in range(2*10**5)] + ['max', 'pop']*10**5)]

        
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