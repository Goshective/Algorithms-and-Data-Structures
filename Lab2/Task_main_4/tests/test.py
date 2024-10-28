import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab2.Task_main_4.src.main import bin_search_loop
from test_utils import output_design


class InsertionSortTestCase(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(bin_search_loop(5, [1, 5, 8, 12, 13], [8, 1, 23, 1, 11]), [2, 0, -1, 0, -1])
        self.assertEqual(bin_search_loop(1, [0], [0, 1]), [0, -1])
    
    def test_time_memory(self):
        output_design(1, bin_search_loop, 1, [0], [0])

        output_design(2, bin_search_loop, 10**3, list(range(10**3)), list(range(10**3)))

        output_design(3, bin_search_loop, 10**5, list(range(10**5)), [0]*10**5)


if __name__ == "__main__":
    unittest.main()