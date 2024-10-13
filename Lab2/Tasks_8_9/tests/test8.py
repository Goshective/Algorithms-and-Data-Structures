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

    def test_correctness_sum(self):
        self.assertEqual(sum_polynoms([1, 2, 3], [3, 4, 5]), [4, 6, 8]) 
        self.assertEqual(sum_polynoms([1, 2, 3], [3, 4, 5], shift_A=1), [3, 5, 7, 3]) # a0 + a1*x + ...
        self.assertEqual(sum_polynoms([1, 2, 3], [3, 4, 5], shift_A=1, shift_B=2), [0, 1, 5, 7, 5])

    def test_correctness_multiply(self):
        self.assertEqual(multiply_polynoms(3, [3, 2, 5][::-1], [5, 1, 2][::-1]), [15, 13, 33, 9, 10][::-1])
        self.assertEqual(multiply_polynoms(5, [2, 5, 3, 1, -1], [1, 2, 2, 3, 6]), [2, 9, 17, 23, 34, 39, 19, 3, -6])
    
    def test_time_memory(self):
        self.output_design(1, multiply_polynoms, [0], 1, [0], [0])

        res = multiply_polynoms(100, [1]* 100, [1, -1]*50)
        self.output_design(2, multiply_polynoms, res, 100, [1]* 100, [1, -1]*50)

        res = multiply_polynoms(500, [1]* 500, [1, -1]*250)
        self.output_design(3, multiply_polynoms, res, 500, [1]* 500, [1, -1]*250)


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(current_dir, '..', 'src')
    sys.path.insert(0, src_dir)

    from task8 import sum_polynoms, multiply_polynoms
    unittest.main()