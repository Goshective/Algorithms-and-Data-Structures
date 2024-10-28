import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab3.Task_plus_5.src.main import solution
from test_utils import output_design

class HirschIndexTestCase(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(solution([3,0,6,1,5]), 3)

        self.assertEqual(solution([1,3,1]), 1)

        self.assertEqual(solution([500,500,600]), 3)
    
    def test_time_memory(self):
        output_design('10 элементов', solution, list(range(10)))

        medium_inp = [100-i for i in range(100)]
        output_design('100 элементов', solution, medium_inp)

        maximum_inp = [(5000-i)//5 for i in range(5000)]
        output_design('5000 элементов', solution, maximum_inp)


if __name__ == "__main__":
    unittest.main()