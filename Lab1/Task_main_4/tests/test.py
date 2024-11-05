import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab1.Task_main_4.src.main import linear_search
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestCaseLinearSearch(unittest.TestCase):
    def test_should_search(self):
        # given
        inp = [1, 2, 3, 4, 1, 2, 3, 1], 1
        # when
        # then
        self.assertEqual(linear_search(*inp), [0, 4, 7])

        # given
        inp = [1, 2, 3, 4, 1, 2, 3, 1], 5
        # when
        # then
        self.assertEqual(linear_search(*inp), [])
    
    def test_should_fit_time_memory_limit(self):
        test_data = [(f'{i} элементов', (list(range(i-1, -1, -1)), 0)) for i in 
                     (10, 100, 1000)]

        expected_memory = 256 * MB
        expected_time = 2

        time_for_tests = []

        for time_mod, memory_mod in ((1, 0), (0, 1)):
            for test_id, (test_name, input_by_size) in enumerate(test_data):

                if time_mod:
                    time_for_tests.append(TM.count_time(linear_search, *input_by_size))

                if memory_mod:

                    # given
                    res_memory = TM.count_memory(linear_search, *input_by_size)
                    res_time = time_for_tests[test_id]

                    # when
                    TM.output_design(test_name, res_time, res_memory)

                    # then
                    self.assertLessEqual(res_time, expected_time)
                    self.assertLessEqual(res_memory, expected_memory)


if __name__ == "__main__":
    unittest.main()