import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab1.Task_plus_9.src.main import bin_sum
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestCaseInsertionSort(unittest.TestCase):
    def test_should_sum(self):
        # given
        a, b = list(map(int, '1000001')), list(map(int, '1111111'))
        # when
        # then
        self.assertEqual(bin_sum(a, b), list(map(int, '11000000')))
        
        # given
        a, b = [0], [0]
        # when
        # then
        self.assertEqual(bin_sum(a, b), [0])

        # given
        a, b = [0], [1]
        # when
        # then
        self.assertEqual(bin_sum(a, b), [1])

        # given
        a, b = [a, b]
        # when
        # then
        self.assertEqual(bin_sum(a, b), [1])

        # given
        a, b = [1], [1]
        # when
        # then
        self.assertEqual(bin_sum(a, b), [1, 0])
    
    def test_should_fit_time_memory_limit(self):
        test_data = [(f'{i} элементов', ([1]*i, [1]*i)) for i in 
                     (10, 100, 1000)]

        expected_memory = 256 * MB
        expected_time = 2

        time_for_tests = []

        for time_mod, memory_mod in ((1, 0), (0, 1)):
            for test_id, (test_name, input_by_size) in enumerate(test_data):

                if time_mod:
                    time_for_tests.append(TM.count_time(bin_sum, *input_by_size))

                if memory_mod:

                    # given
                    res_memory = TM.count_memory(bin_sum, *input_by_size)
                    res_time = time_for_tests[test_id]

                    # when
                    TM.output_design(test_name, res_time, res_memory)

                    # then
                    self.assertLessEqual(res_time, expected_time)
                    self.assertLessEqual(res_memory, expected_memory)


if __name__ == "__main__":
    unittest.main()