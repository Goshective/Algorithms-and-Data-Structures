import unittest
import sys
import os
import time
import tracemalloc
from random import shuffle

class RandomizedQuickSortTestCase(unittest.TestCase):
    def output_design(self, test_name, func, ln, lst):
        t_start = time.perf_counter()
        tracemalloc.start()
        func(lst, 0, ln - 1)

        print(f"Тест {test_name}:")
        print("Время работы: %s секунд " % (time.perf_counter() - t_start), end='\n')
        print("Затрачено памяти:", round(tracemalloc.get_traced_memory()[1]/(1024*1024), 3), "Мегабайт")
        tracemalloc.stop()

    def test_correctness(self):
        inp = [31, 41, 59, 26, 41, 58]
        sort_func(inp, 0, len(inp) - 1)
        self.assertEqual(inp, [26, 31, 41, 41, 58, 59])

        inp = [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]
        sort_func(inp, 0, len(inp) - 1)
        self.assertEqual(inp, list(range(10)))
    
    def test_time_memory(self):
        minimum_inp = list(range(100))
        self.output_design('100 элементов', sort_func, 100, minimum_inp)

        medium_inp = list(range(1000))
        shuffle(medium_inp)
        self.output_design('1000 элементов', sort_func, 1000, medium_inp)

        medium_inp = list(range(10**4))
        shuffle(medium_inp)
        self.output_design('10e4 элементов', sort_func, 10**4, medium_inp)

        medium_inp = list(range(10**5))
        shuffle(medium_inp)
        self.output_design('10e5 элементов', sort_func, 10**5, medium_inp)

        maximum_inp = [x * 100 for x in range(10**5-1, -1, -1)]
        self.output_design('10e5 элементов (обратно)', sort_func, 10**5, maximum_inp)


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(current_dir, '..', 'src')
    sys.path.insert(0, src_dir)

    from main import RandomizedQuickSort as sort_func
    unittest.main()