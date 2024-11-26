import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab6.Task_main_2.src.main import solution
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestsHashTable(unittest.TestCase):
    def test_should_find_none_and_check_removed(self):
        # given
        inp = [
            "find 3839442",
            "add 123456 me",
            "add 0 granny",
            "find 0",
            "find 123456",
            "del 0",
            "del 0",
            "find 0"
        ]
        expected_res = [
            "not found",
            "granny",
            "me",
            "not found"
        ]

        # when
        res = solution(inp)

        # then
        self.assertEqual(res, expected_res)

    def test_should_find_none_and_check_removed(self):
        # given
        inp = [
            "add 911 police",
            "add 76213 Mom",
            "add 17239 Bob",
            "find 76213",
            "find 910",
            "find 911",
            "del 910",
            "del 911",
            "find 911",
            "find 76213",
            "add 76213 daddy",
            "find 76213"
        ]
        expected_res = [
            "Mom",
            "not found",
            "police",
            "not found",
            "Mom",
            "daddy"
        ]

        # when
        res = solution(inp)

        # then
        self.assertEqual(res, expected_res)

    def check_time_memory_limit(self, res_time, res_memory):
        # given
        expected_memory = 256 * MB
        expected_time = 3
        # when
        # then
        
        self.assertLessEqual(res_time, expected_time)
        self.assertLessEqual(res_memory, expected_memory)
    
    def test_should_fit_time_memory_limit(self):
        # given
        test_data = []
        for title, n in (('100 элементов', 100), ('10e3 элементов', 1000), ('10e5 элементов', 10**5)):
            data = [f'add {101*i} a' for i in range(n // 2)] + [f'find {101*i} a' for i in range(n // 4)]
            data += [f'del {101*i} a' for i in range(n // 4)]
            test_data.append((title, data))

        for test_name, input_by_size in test_data:
            # when
            res_time = TM.count_time(solution, input_by_size)
            res_memory = TM.count_memory(solution, input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)


if __name__ == "__main__":
    unittest.main()