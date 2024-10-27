import unittest
import sys
import os
import time
import tracemalloc
from random import randint

class MultiArrayTestCase(unittest.TestCase):
    def output_design(self, test_name, func, *args):
        t_start = time.perf_counter()
        tracemalloc.start()
        func(*args)

        print(f"Тест {test_name}:")
        print("Время работы: %s секунд " % (time.perf_counter() - t_start), end='\n')
        print("Затрачено памяти:", round(tracemalloc.get_traced_memory()[1]/(1024*1024), 3), "Мегабайт")
        tracemalloc.stop()

    def test_correctness(self):
        a, b = [7, 1, 4, 9], [2, 7, 8, 11]
        self.assertEqual(solution(4, 4, a, b, qsort), 51)
    
    def test_time_memory(self):
        for func_name, func in (('\nQuick sort (Python):', qsort), ('\nRadix sort:', radix_sort)):
            print(func_name)
            a, b = [7, 1, 4, 9], [2, 7, 8, 11]
            self.output_design('10 элементов', solution, 4, 4, a, b, func)

            a, b = list(range(100, 0, -1)), list(range(100, 0, -1))
            self.output_design('100^2 элементов', solution, 100, 100, a, b, func)

            a, b = list(range(1000, 0, -1)), list(range(1000, 0, -1))
            self.output_design('6000^2 элементов', solution, 1000, 1000, a, b, func)


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(current_dir, '..', 'src')
    sys.path.insert(0, src_dir)

    from main import (solution, 
                      cross_multiplication, 
                      qsort,
                      radix_sort
                      )
    unittest.main()