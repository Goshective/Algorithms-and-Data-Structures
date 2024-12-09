import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab7.Task_plus_7.src.main import solution
from test_utils import (
    ConsoleTimeMemory as TM, 
    get_task_name,
    MB
)


class TestsPatterns(unittest.TestCase):
    def test_should_fit(self):
        # given
        inp = 'k?t*n', 'kitten'
        expected_res = 'YES'

        # when
        res = solution(*inp)
        # then
        self.assertEqual(res, expected_res)

    def test_should_not_fit(self):
        # given
        inp = 'k?t?n', 'kitten'
        expected_res = 'NO'

        # when
        res = solution(*inp)
        # then
        self.assertEqual(res, expected_res)


    def test_should_check_multiple_stars(self):
        # given
        inp = 'a*a*ca??b**a', 'abracadabra'
        expected_res = 'YES'

        # when
        res = solution(*inp)
        # then
        self.assertEqual(res, expected_res)

    def test_should_check_empty_wrong(self):
        # given
        inp = '?', ''
        expected_res = 'NO'

        # when
        res = solution(*inp)
        # then
        self.assertEqual(res, expected_res)

    def test_should_check_empty_right(self):
        # given
        inp = '**', ''
        expected_res = 'YES'

        # when
        res = solution(*inp)
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
        test_data = [(f'{i} символов', ('a?a*'*(i//4), 'aba'*(i//3 + 1))) for i in (100, 1000, 2500)]

        
        print()
        print('-'*55)
        print(get_task_name(PATH))

        for test_name, input_by_size in test_data:
            # when
            res_time = TM.count_time(solution, *input_by_size)
            res_memory = TM.count_memory(solution, *input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)

        print('-'*55)


if __name__ == "__main__":
    unittest.main()