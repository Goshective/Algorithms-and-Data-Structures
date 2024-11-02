import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab3.Task_main_2.src.main import solution
from test_utils import output_design


class TestCaseSegments(unittest.TestCase):
    def test_shold_find__the_worst_case(self):
        # given
        inp = 3
        # when
        # then
        self.assertEqual(solution(inp), [1, 3, 2])

        # given
        inp = 4
        # when
        # then
        self.assertEqual(solution(inp), [1, 4, 2, 3])

        # given
        inp = 5
        # when
        # then
        self.assertEqual(solution(inp), [1, 4, 5, 3, 2])
    
    def test_should_fit_time_memory_limit(self):
        # given
        minimum_input = 10
        # when
        # then
        output_design('10 элементов', solution, minimum_input)

        # given
        medium_input = 1000
        # when
        # then
        output_design('1000 элементов', solution, medium_input)

        # given
        maximum_input = 4*10**5
        # when
        # then
        output_design('10e6 элементов', solution, maximum_input)


if __name__ == "__main__":
    unittest.main()