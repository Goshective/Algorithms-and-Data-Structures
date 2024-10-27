import unittest
import sys
import os
import time
import tracemalloc

class SegmentsTestCase(unittest.TestCase):
    def output_design(self, test_name, func, *args):
        t_start = time.perf_counter()
        tracemalloc.start()
        func(*args)

        print(f"Тест {test_name}:")
        print("Время работы: %s секунд " % (time.perf_counter() - t_start), end='\n')
        print("Затрачено памяти:", round(tracemalloc.get_traced_memory()[1]/(1024*1024), 3), "Мегабайт")
        tracemalloc.stop()

    def test_correctness(self):
        res = solution(2, 3, [[0, 5], [7, 10]], [1, 6, 11])
        self.assertEqual(res, [1, 0, 0])

        res = solution(1, 3, [[-10, 10]], [-100, 100, 0])
        self.assertEqual(res, [0, 0, 1])

        res = solution(3, 2, [[0, 5], [-3, 2], [7, 10]], [1, 6])
        self.assertEqual(res, [2, 0])
    
    def test_time_memory(self):
        self.output_design('10 элементов', solution, 2, 3, [[0, 5], [7, 10]], [1, 6, 11])

        medium_inp = [[2*i, 2*i+1] for i in range(1000)]
        self.output_design('1000 элементов', solution, 1000, 1000, medium_inp, list(range(1000)))

        maximum_inp = [[2*i, 2*i+1] for i in range(50000)]
        self.output_design('5*10e4 элементов', solution, 50000, 50000, maximum_inp, list(range(50000)))


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(current_dir, '..', 'src')
    sys.path.insert(0, src_dir)

    from main import solution
    unittest.main()