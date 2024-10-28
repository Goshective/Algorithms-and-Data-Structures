import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab3.Task_main_4.src.main import solution
from test_utils import output_design


class SegmentsTestCase(unittest.TestCase):
    def test_correctness(self):
        res = solution(2, 3, [[0, 5], [7, 10]], [1, 6, 11])
        self.assertEqual(res, [1, 0, 0])

        res = solution(1, 3, [[-10, 10]], [-100, 100, 0])
        self.assertEqual(res, [0, 0, 1])

        res = solution(3, 2, [[0, 5], [-3, 2], [7, 10]], [1, 6])
        self.assertEqual(res, [2, 0])
    
    def test_time_memory(self):
        output_design('10 элементов', solution, 2, 3, [[0, 5], [7, 10]], [1, 6, 11])

        medium_inp = [[2*i, 2*i+1] for i in range(1000)]
        output_design('1000 элементов', solution, 1000, 1000, medium_inp, list(range(1000)))

        maximum_inp = [[2*i, 2*i+1] for i in range(50000)]
        output_design('5*10e4 элементов', solution, 50000, 50000, maximum_inp, list(range(50000)))


if __name__ == "__main__":
    unittest.main()