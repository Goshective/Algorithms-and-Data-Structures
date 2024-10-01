import unittest
import sys
import os
import time
import tracemalloc
from random import shuffle

class InsertionSortTestCase(unittest.TestCase):
    def output_design(self, test_name, func, ln, lst):
        t_start = time.perf_counter()
        tracemalloc.start()
        func(lst, 0, ln - 1)

        print(f"Тест {test_name}:")
        print("Время работы: %s секунд " % (time.perf_counter() - t_start), end='\n')
        print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
        tracemalloc.stop()

    def test_correctness(self):
        inp = [31, 41, 59, 26, 41, 58]
        merge_sort(inp, 0, len(inp) - 1)
        self.assertEqual(inp, [26, 31, 41, 41, 58, 59])

        inp = [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]
        merge_sort(inp, 0, len(inp) - 1)
        self.assertEqual(inp, list(range(10)))
    
    def test_time_memory(self):
        minimum_inp = list(range(100))
        self.output_design('100 элементов', merge_sort, 100, minimum_inp)
        self.assertEqual(minimum_inp, list(range(100)))

        medium_inp = list(range(1000))
        shuffle(medium_inp)
        self.output_design('1000 элементов', merge_sort, 1000, medium_inp)
        self.assertEqual(medium_inp, list(range(1000)))

        maximum_inp = [x * 5*10**4 for x in range(2*10**4-1, -1, -1)]
        self.output_design('2*10e4 элементов', merge_sort, 2*10**4, maximum_inp)
        self.assertEqual(maximum_inp, list(range(0, 10**9, 5*10**4)))
        


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(current_dir, '..', 'src')
    sys.path.insert(0, src_dir)

    from task1 import merge_sort
    unittest.main()