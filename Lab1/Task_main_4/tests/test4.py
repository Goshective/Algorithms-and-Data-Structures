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
        self.assertEqual(linear_search([1, 2, 3, 4, 1, 2, 3, 1], 1), [0, 4, 7])

        self.assertEqual(linear_search([1, 2, 3, 4, 1, 2, 3, 1], 5), [])
    
    def test_time_memory(self):
        self.output_design(1, linear_search, [4], list(range(10)), 4)

        self.output_design(2, linear_search, [], list(range(10**3)), 10**3)


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(current_dir, '..', 'src')
    sys.path.insert(0, src_dir)

    from task4 import linear_search
    unittest.main()