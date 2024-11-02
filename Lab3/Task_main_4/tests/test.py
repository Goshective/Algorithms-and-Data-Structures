import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab3.Task_main_4.src.main import solution
from test_utils import output_design


class SegmentsTestCase(unittest.TestCase):
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
        # given
        minimum_inp = [[0, 5], [7, 10]]
        # when
        # then
        output_design('10 элементов', solution, 2, 3, minimum_inp, [1, 6, 11])

        # given
        medium_inp = [[2*i, 2*i+1] for i in range(1000)]
        # when
        # then
        output_design('1000 элементов', solution, 1000, 1000, medium_inp, list(range(1000)))

        # given
        maximum_inp = [[2*i, 2*i+1] for i in range(50000)]
        # when
        # then
        output_design('5*10e4 элементов', solution, 50000, 50000, maximum_inp, list(range(50000)))


if __name__ == "__main__":
    unittest.main()