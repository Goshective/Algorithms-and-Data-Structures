import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab5.Task_main_3.src.main import solution
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestsPackages(unittest.TestCase):
    def test_should_check_empty(self):
        # given
        inp = 1, []
        excepted_res = []

        # when
        res = solution(*inp)

        # then
        self.assertEqual(res, excepted_res)

    def test_should_execute_1(self):
        # given
        inp = 1, ['0 0']
        excepted_res = [0]

        # when
        res = solution(*inp)

        # then
        self.assertEqual(res, excepted_res)

    def test_should_check_buffer(self):
        # given
        inp = (1, 
               ['0 1',
                '0 1']
                   )
        excepted_res = [0, -1]

        # when
        res = solution(*inp)

        # then
        self.assertEqual(res, excepted_res)

    def test_should_execute_and_receive(self):
        # given
        inp = (1, 
               ['0 1',
                '1 1']
                   )
        excepted_res = [0, 1]

        # when
        res = solution(*inp)

        # then
        self.assertEqual(res, excepted_res)

    def test_should_return_start_time(self):
        # given
        inp = (1, 
                ['0 1']
                   )
        excepted_res = [0]

        # when
        res = solution(*inp)

        # then
        self.assertEqual(res, excepted_res)

    def test_should_check_big_gaps(self):
        # given
        inp = (1, 
               ['0 1',
                '3 1',
                '10 1']
                   )
        excepted_res = [0, 3, 10]

        # when
        res = solution(*inp)

        # then
        self.assertEqual(res, excepted_res)

    def test_should_check_simultaneous_input_even_if_instant_process(self):
        # given
        inp = (1, 
               ['0 1',
                '0 0']
                   )
        excepted_res = [0, -1]

        # when
        res = solution(*inp)

        # then
        self.assertEqual(res, excepted_res)

    def test_should_check_filling_the_buffer(self):
        # given
        inp = (3, 
               ['0 1',
               '1 2',
               '2 2',
               '3 2',
               '4 2',
               '5 2'])
        excepted_res = [0, 2, 4, 6, 8, -1]

        # when
        res = solution(*inp)

        # then
        self.assertEqual(res, excepted_res)

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
        test_data = [('100 элементов', (25, [f'{20*i} {21*i}' for i in range(100)])),
                     ('10e3 элементов', (250, [f'{20*i} {21*i}' for i in range(10**3)])),
                     ('10e5 элементов', (25*10**4, [f'{20*i} {21*i}' for i in range(10**5)])),]

        for test_name, input_by_size in test_data:
            # when
            res_time = TM.count_time(solution, *input_by_size)
            res_memory = TM.count_memory(solution, *input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)


if __name__ == "__main__":
    unittest.main()