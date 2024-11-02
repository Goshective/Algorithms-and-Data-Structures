import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab3.Task_plus_5.src.main import solution
from test_utils import output_design


class HirschIndexTestCase(unittest.TestCase):
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
        # given
        minimum_inp = list(range(10))
        # when
        # then
        output_design('10 элементов', solution, minimum_inp)

        # given
        medium_inp = [100-i for i in range(100)]
        # when
        # then
        output_design('100 элементов', solution, medium_inp)

        # given
        maximum_inp = [(5000-i)//5 for i in range(5000)]
        # when
        # then
        output_design('5000 элементов', solution, maximum_inp)


if __name__ == "__main__":
    unittest.main()