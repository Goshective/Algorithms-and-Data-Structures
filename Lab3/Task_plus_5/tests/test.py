import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab3.Task_plus_5.src.main import solution
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestCaseHirschIndex(unittest.TestCase):
    def test_find_hirsch_index(self):
        # given
        inp = [3,0,6,1,5]
        # when
        # then
        self.assertEqual(solution(inp), 3)

        # given
        inp = [1,3,1]
        # when
        # then
        self.assertEqual(solution(inp), 1)

        # given
        inp = [500,500,600]
        # when
        # then
        self.assertEqual(solution(inp), 3)
    
    def test_should_fit_time_memory_limit(self):
        minimum_inp = list(range(10))
        medium_inp = [100 - i for i in range(100)]
        maximum_inp = [(5000 - i) // 5 for i in range(5000)]

        test_data = [('10 элементов', minimum_inp),
                     ('100 элементов', medium_inp),
                     ('5000 элементов', maximum_inp)]
        
        expected_memory = 256 * MB
        expected_time = 2

        time_for_tests = []

        for time_mod, memory_mod in ((1, 0), (0, 1)):
            for test_id, (test_name, input_by_size) in enumerate(test_data):

                if time_mod:
                    time_for_tests.append(TM.count_time(solution, input_by_size))

                if memory_mod:

                    # given
                    res_memory = TM.count_memory(solution, input_by_size)
                    res_time = time_for_tests[test_id]

                    # when
                    TM.output_design(test_name, res_time, res_memory)

                    # then
                    self.assertLessEqual(res_time, expected_time)
                    self.assertLessEqual(res_memory, expected_memory)


if __name__ == "__main__":
    unittest.main()