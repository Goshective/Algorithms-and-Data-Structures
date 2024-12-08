import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))


from Lab7.Task_main_6.src.main import solution

from test_utils import (ConsoleTimeMemory as TM, MB)


class TestLIS(unittest.TestCase):
    def test_should_find_basic_LIS(self):
        # given

        inp = [3, 29, 5, 5, 28, 6]
        expected_res = 3

        # when

        res = len(solution(inp))

        # then

        self.assertEqual(res, expected_res)

    def test_should_find_only_increasing_sequence(self):
        # given

        inp = [100, 90, 80, 80, 81, 82, 83, 70, 60, 50]
        expected_res = [80, 81, 82, 83]

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
        test_data = [('100 элементов', [(-1)**(i%2) * i for i in range(100)]),
                     ('5000 элементов', [(-1)**(i%2) * i for i in range(5000)]),
                     ('3*10e5 элементов', [(-1)**(i%2) * i * 3 * 10**3 for i in range(3 * 10 ** 5)])]

        for test_name, input_by_size in test_data:
            # when
            res_time = TM.count_time(solution, input_by_size)
            res_memory = TM.count_memory(solution, input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)


if __name__ == "__main__":
    unittest.main()