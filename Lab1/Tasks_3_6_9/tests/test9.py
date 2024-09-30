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
        self.assertEqual(bin_sum(list(map(int, '1000001')), list(map(int, '1111111'))), list(map(int, '11000000')))
        self.assertEqual(bin_sum([0], [0]), [0])
        self.assertEqual(bin_sum([0], [1]), [1])
        self.assertEqual(bin_sum([1], [0]), [1])
        self.assertEqual(bin_sum([1], [1]), [1, 0])
    
    def test_time_memory(self):
        self.output_design(1, bin_sum, [1], [0], [1])

        self.output_design(2, bin_sum, [1]*10**3+[0], [1]*10**3, [1]*10**3)


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(current_dir, '..', 'src')
    sys.path.insert(0, src_dir)

    from task9 import bin_sum
    unittest.main()