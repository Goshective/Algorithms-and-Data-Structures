import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab4.Task_main_4.src.main import solution
from test_utils import (
    ConsoleTimeMemory as TM, 
    get_task_name,
    MB
)


class TestsBrackets(unittest.TestCase):
    def test_should_find_wrong_index_for_len_1(self):
        # given
        inp = '{'
        expected_res = 1

        # when
        res = solution(inp)

        # then
        self.assertEqual(res, expected_res)

    def test_should_find_wrong_index_for_multiple_brackets(self):
        # given
        inp = '{[}'
        expected_res = 3

        # when
        res = solution(inp)

        # then
        self.assertEqual(res, expected_res)

    def test_should_find_wrong_index_for_multiple_brackets_with_letters(self):
        # given
        inp = 'foo(bar[i);'
        expected_res = 10

        # when
        res = solution(inp)

        # then
        self.assertEqual(res, expected_res)

    def test_should_return_success(self):
        # given
        inp = '[]'
        expected_res = 'Success'

        # when
        res = solution(inp)

        # then
        self.assertEqual(res, expected_res)

    def test_should_return_success_multiple_brackets(self):
        # given
        inp = '{}[]'
        expected_res = 'Success'

        # when
        res = solution(inp)

        # then
        self.assertEqual(res, expected_res)

    def test_should_return_success_recursion(self):
        # given
        inp = '[()]'
        expected_res = 'Success'

        # when
        res = solution(inp)

        # then
        self.assertEqual(res, expected_res)

    def test_should_return_success_with_letters(self):
        # given
        inp = 'foo(bar);'
        expected_res = 'Success'

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
        test_data = [('100 элементов', '('*5*10 + ')'*5*10),
                     ('10e4 элементов', '('*5*10**3 + ')'*5*10**3),
                     ('10e6 элементов', '('*5*10**5 + ')'*5*10**5)]

        
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