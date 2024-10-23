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
        self.assertEqual(solution(5, [2, 3, 9, 2, 2]), 1)
        self.assertEqual(solution(4, [1, 2, 3, 4]), 0)
        self.assertEqual(solution(9, [0, 3, 9, 2, 2, 2, 2, 2, 2]), 1)
        self.assertEqual(solution(9, [0, 3, 0, 3, 0, 3, 0, 3, 0]), 1)
        self.assertEqual(solution(9, [0, 3, 0, 3, 0, 3, 0, 3, 1]), 0)
    
    def test_time_memory(self):
        self.output_design(1, solution, 0, 4, [1, 2, 3, 4])

        self.output_design(2, solution, 0, 10**3, list(range(10**3)))

        self.output_design(3, solution, 1, 5*10**4, [100]*5*10**4)


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(current_dir, '..', 'src')
    sys.path.insert(0, src_dir)

    from task5 import solution
    unittest.main()