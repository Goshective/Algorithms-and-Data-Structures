import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab2.Task_plus_5.src.main import solution
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestCaseInsertionSort(unittest.TestCase):
    def test_should_be_over_the_half(self):
        # given
        inp = [2, 3, 9, 2, 2]
        # when
        # then
        self.assertEqual(solution(len(inp), inp), 1)

        # given
        inp = [1, 2, 3, 4]
        # when
        # then
        self.assertEqual(solution(len(inp), inp), 0)

        # given
        inp = [0, 3, 9, 2, 2, 2, 2, 2, 2]
        # when
        # then
        self.assertEqual(solution(len(inp), inp), 1)

        # given
        inp = [0, 3, 0, 3, 0, 3, 0, 3, 0]
        # when
        # then
        self.assertEqual(solution(len(inp), inp), 1)

        # given
        inp = [0, 3, 0, 3, 0, 3, 0, 3, 1]
        # when
        # then
        self.assertEqual(solution(len(inp), inp), 0)
    
    def test_should_fit_time_memory_limit(self):
        test_data = [(f'{i} элементов', (i, list(range(i)))) for i in 
                     (10, 1000, 10**5)]

        expected_memory = 256 * MB
        expected_time = 2

        time_for_tests = []

        for time_mod, memory_mod in ((1, 0), (0, 1)):
            for test_id, (test_name, input_by_size) in enumerate(test_data):

                if time_mod:
                    time_for_tests.append(TM.count_time(solution, *input_by_size))

                if memory_mod:

                    # given
                    res_memory = TM.count_memory(solution, *input_by_size)
                    res_time = time_for_tests[test_id]

                    # when
                    TM.output_design(test_name, res_time, res_memory)

                    # then
                    self.assertLessEqual(res_time, expected_time)
                    self.assertLessEqual(res_memory, expected_memory)


if __name__ == "__main__":
    unittest.main()