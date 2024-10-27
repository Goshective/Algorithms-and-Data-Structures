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
        self.assertEqual(solution(3), [1, 3, 2])

        self.assertEqual(solution(4), [1, 4, 2, 3])

        self.assertEqual(solution(5), [1, 4, 5, 3, 2])
    
    def test_time_memory(self):
        self.output_design('10 элементов', solution, 10)

        self.output_design('1000 элементов', solution, 1000)

        self.output_design('10e6 элементов', solution, 4*10**5)


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(current_dir, '..', 'src')
    sys.path.insert(0, src_dir)

    from main import solution
    unittest.main()