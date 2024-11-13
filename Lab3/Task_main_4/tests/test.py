import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab3.Task_main_4.src.main import solution
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestCaseSegments(unittest.TestCase):
    def test_should_find_intersections(self):
        # given
        inp = [[0, 5], [7, 10]], [1, 6, 11]
        expected_res = [1, 0, 0]

        # when
        res = solution(len(inp[0]), len(inp[1]), *inp)

        # then
        self.assertEqual(res, expected_res)

    def test_should_find_distant_edges(self):
        # given
        inp = [[-10, 10]], [-100, 100, 0]
        expected_res = [0, 0, 1]

        # when
        res = solution(len(inp[0]), len(inp[1]), *inp)
        
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
        test_data = []

        minimum_inp = [[0, 5], [7, 10]]
        test_data.append(('10 элементов', (2, 3, minimum_inp, [1, 6, 11])))

        medium_inp = [[2*i, 2*i+1] for i in range(1000)]
        test_data.append(('1000 элементов', (1000, 1000, medium_inp, list(range(1000)))))

        maximum_inp = [[2*i, 2*i+1] for i in range(50000)]
        test_data.append(('5*10e4 элементов', (50000, 50000, maximum_inp, list(range(50000)))))

        for test_name, input_by_size in test_data:
            # when
            res_time = TM.count_time(solution, *input_by_size)
            res_memory = TM.count_memory(solution, *input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)


if __name__ == "__main__":
    unittest.main()