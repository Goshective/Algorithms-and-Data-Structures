import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab1.Task_plus_6.src.main import bubble_sort as sort_func
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestCaseBubbleSort(unittest.TestCase):
    def test_should_sort(self):
        # given
        inp = [31, 41, 59, 26, 41, 58]
        # when
        sort_func(len(inp), inp)
        # then
        self.assertEqual(inp, [26, 31, 41, 41, 58, 59])

        # given
        inp = [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]
        # when
        sort_func(len(inp), inp)
        # then
        self.assertEqual(inp, list(range(10)))
    
    def test_should_fit_time_memory_limit(self):
        test_data = [(f'{i} элементов', (i, list(range(i)))) for i in 
                     (10, 100, 1000)]

        expected_memory = 256 * MB
        expected_time = 2

        time_for_tests = []

        for time_mod, memory_mod in ((1, 0), (0, 1)):
            for test_id, (test_name, input_by_size) in enumerate(test_data):

                if time_mod:
                    time_for_tests.append(TM.count_time(sort_func, *input_by_size))

                if memory_mod:

                    # given
                    res_memory = TM.count_memory(sort_func, *input_by_size)
                    res_time = time_for_tests[test_id]

                    # when
                    TM.output_design(test_name, res_time, res_memory)

                    # then
                    self.assertLessEqual(res_time, expected_time)
                    self.assertLessEqual(res_memory, expected_memory)
        


if __name__ == "__main__":
    unittest.main()