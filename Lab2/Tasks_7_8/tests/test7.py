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
        self.assertEqual(solution(17, [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]),
                          (7, 11, 43))
    
    def test_time_memory(self):
        self.output_design(1, solution, (0, 1, 1), 2, [0, 1])

        self.output_design(2, solution, (0, 10**3-1, 10**3-1), 10**3, list(range(10**3)))

        self.output_design(3, solution, (0, 10**4-1, 10**4-1), 10**4, list(range(10**4)))


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(current_dir, '..', 'src')
    sys.path.insert(0, src_dir)

    from task7 import solution
    unittest.main()