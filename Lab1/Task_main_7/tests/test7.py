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
        self.assertEqual(find_info(5, [10.00, 8.70, 0.01, 5.00, 3.00]), (3, 4, 1))

        self.assertEqual(find_info(9, [1, 2, 3, 4, 5, 6, 7, 8, 9]), (1, 5, 9))
    
    def test_time_memory(self):
        self.output_design(1, find_info, (1, 5, 9), 9, list(range(1,10)))

        self.output_design(2, find_info, (999, 500, 1), 10**3-1, list(range(10**3-1, 0, -1)))


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(current_dir, '..', 'src')
    sys.path.insert(0, src_dir)

    from task7 import find_info
    unittest.main()