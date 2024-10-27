import unittest
import sys
import os
import time
import tracemalloc
from random import randint

class PointsTestCase(unittest.TestCase):
    def output_design(self, test_name, func, *args):
        t_start = time.perf_counter()
        tracemalloc.start()
        func(*args)

        print(f"Тест {test_name}:")
        print("Время работы: %s секунд " % (time.perf_counter() - t_start), end='\n')
        print("Затрачено памяти:", round(tracemalloc.get_traced_memory()[1]/(1024), 3), "Килобайт")
        tracemalloc.stop()

    def test_correctness(self):
        self.assertEqual(solution(3, 2, [[3, 3], [-2, 4], [5, -1]]), [[3, 3], [-2, 4]])

        self.assertEqual(solution(2, 1, [[1,3], [-2,2]]), [[-2,2]])

        self.assertEqual(solution(3, 0, [[3, 3], [-2, 4], [5, -1]]), [])
    
    def test_time_memory(self):
        self.output_design('10 элементов', solution, 10, 10, [[0, i] for i in range(10)])

        medium_inp = [[randint(-100, 100), randint(-100, 100)] for _ in range(1000)]
        self.output_design('1000 элементов', solution, 1000, 1000, medium_inp)

        maximum_inp = [[randint(-10**4, 10**4), randint(-10**4, 10**4)] for _ in range(10**5)]
        self.output_design('5000 элементов', solution, 10**5, 10**5, maximum_inp)


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(current_dir, '..', 'src')
    sys.path.insert(0, src_dir)

    from main import solution
    unittest.main()