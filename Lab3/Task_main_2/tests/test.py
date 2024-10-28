import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab3.Task_main_2.src.main import solution
from test_utils import output_design


class SegmentsTestCase(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(solution(3), [1, 3, 2])

        self.assertEqual(solution(4), [1, 4, 2, 3])

        self.assertEqual(solution(5), [1, 4, 5, 3, 2])
    
    def test_time_memory(self):
        output_design('10 элементов', solution, 10)

        output_design('1000 элементов', solution, 1000)

        output_design('10e6 элементов', solution, 4*10**5)


if __name__ == "__main__":
    unittest.main()