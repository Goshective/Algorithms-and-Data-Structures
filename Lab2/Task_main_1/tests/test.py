import unittest
import sys
import os
from random import shuffle

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab2.Task_main_1.src.main import merge_sort as sort_func
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestCaseInsertionSort(unittest.TestCase):
    def test_should_sort(self):
        # given
        inp = [31, 41, 59, 26, 41, 58]
        # when
        sort_func(inp, 0, len(inp) - 1)
        # then
        self.assertEqual(inp, [26, 31, 41, 41, 58, 59])

        # given
        inp = [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]
        # when
        sort_func(inp, 0, len(inp) - 1)
        # then
        self.assertEqual(inp, list(range(10)))
    
    def test_should_fit_time_memory_limit(self):
        test_data = []

        minimum_inp = list(range(100))
        test_data.append(('100 элементов', (minimum_inp, 0, len(minimum_inp) - 1)))

        medium_inp = list(range(10**4))
        shuffle(medium_inp)
        test_data.append(('10000 элементов', (medium_inp, 0, len(medium_inp) - 1)))

        maximum_inp = [x * 100 for x in range(2*10**4-1, -1, -1)]
        test_data.append(('2*10e4 элементов', (maximum_inp, 0, len(maximum_inp) - 1)))
        

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