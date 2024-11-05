import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab2.Task_main_4.src.main import bin_search_loop
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestCaseInsertionSort(unittest.TestCase):
    def test_should_find(self):
        # given
        # when
        res = bin_search_loop(5, [1, 5, 8, 12, 13], [8, 1, 23, 1, 11])
        # then
        self.assertEqual(res, [2, 0, -1, 0, -1])

        # given
        # when
        res = bin_search_loop(1, [0], [0, 1])
        # then
        self.assertEqual(bin_search_loop(1, [0], [0, 1]), [0, -1])
    
    def test_should_fit_time_memory_limit(self):
        test_data = [(f'{i} элементов', (i, list(range(i)), [0]*i)) for i in 
                     (10, 1000, 10**5)]

        expected_memory = 256 * MB
        expected_time = 2

        time_for_tests = []

        for time_mod, memory_mod in ((1, 0), (0, 1)):
            for test_id, (test_name, input_by_size) in enumerate(test_data):

                if time_mod:
                    time_for_tests.append(TM.count_time(bin_search_loop, *input_by_size))

                if memory_mod:

                    # given
                    res_memory = TM.count_memory(bin_search_loop, *input_by_size)
                    res_time = time_for_tests[test_id]

                    # when
                    TM.output_design(test_name, res_time, res_memory)

                    # then
                    self.assertLessEqual(res_time, expected_time)
                    self.assertLessEqual(res_memory, expected_memory)


if __name__ == "__main__":
    unittest.main()