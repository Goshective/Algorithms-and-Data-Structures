import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab2.Task_plus_7.src.main import solution
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestCaseMaxSubarrayLinear(unittest.TestCase):
    def test_find_subarray_points(self):
        # given
        arr = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
        # when
        # then
        self.assertEqual(solution(len(arr), arr),
                          (7, 11, 43))
    
    def test_should_fit_time_memory_limit(self):
        test_data = [(f'{i} элементов', (i, list(range(i)))) for i in 
                     (10, 1000, 10**4)]

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