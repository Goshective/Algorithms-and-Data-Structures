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
        # when
        # then
        self.assertEqual(solution(2, 3, *inp), [1, 0, 0])

        # given
        inp = [[-10, 10]], [-100, 100, 0]
        # when
        # then
        self.assertEqual(solution(1, 3, *inp), [0, 0, 1])

        # given
        inp = [[0, 5], [-3, 2], [7, 10]], [1, 6]
        # when
        # then
        self.assertEqual(solution(3, 2, *inp), [2, 0])
    
    def test_should_fit_time_memory_limit(self):
        test_data = []

        minimum_inp = [[0, 5], [7, 10]]
        test_data.append(('10 элементов', (2, 3, minimum_inp, [1, 6, 11])))

        medium_inp = [[2*i, 2*i+1] for i in range(1000)]
        test_data.append(('1000 элементов', (1000, 1000, medium_inp, list(range(1000)))))

        maximum_inp = [[2*i, 2*i+1] for i in range(50000)]
        test_data.append(('5*10e4 элементов', (50000, 50000, maximum_inp, list(range(50000)))))

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