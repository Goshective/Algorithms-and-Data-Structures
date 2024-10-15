import unittest
import sys
import os
import time
import tracemalloc

class InsertionSortTestCase(unittest.TestCase):

    def output_design(self, test_num, func, eq_value, *params):
        t_start = time.perf_counter()
        tracemalloc.start()
        self.assertEqual(func(*params), eq_value)

        print(f"Тест {test_num}:")
        print("Время работы: %s секунд " % (time.perf_counter() - t_start), end='\n')
        print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
        tracemalloc.stop()

    def test_correctness(self):
        self.assertEqual(bin_search_loop(5, [1, 5, 8, 12, 13], [8, 1, 23, 1, 11]), [2, 0, -1, 0, -1])
        self.assertEqual(bin_search_loop(1, [0], [0, 1]), [0, -1])
    
    def test_time_memory(self):
        self.output_design(1, bin_search_loop, [0], 1, [0], [0])

        self.output_design(2, bin_search_loop, list(range(10**3)), 10**3, list(range(10**3)), list(range(10**3)))

        self.output_design(3, bin_search_loop, [0]*10**5, 10**5, list(range(10**5)), [0]*10**5)


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(current_dir, '..', 'src')
    sys.path.insert(0, src_dir)

    from task4 import bin_search_loop
    unittest.main()