import unittest
import sys
import os
import time
import tracemalloc

class HirschIndexTestCase(unittest.TestCase):
    def output_design(self, test_name, func, *args):
        t_start = time.perf_counter()
        tracemalloc.start()
        func(*args)

        print(f"Тест {test_name}:")
        print("Время работы: %s секунд " % (time.perf_counter() - t_start), end='\n')
        print("Затрачено памяти:", round(tracemalloc.get_traced_memory()[1]/(1024), 3), "Килобайт")
        tracemalloc.stop()

    def test_correctness(self):
        self.assertEqual(solution([3,0,6,1,5]), 3)

        self.assertEqual(solution([1,3,1]), 1)

        self.assertEqual(solution([500,500,600]), 3)
    
    def test_time_memory(self):
        self.output_design('10 элементов', solution, list(range(10)))

        medium_inp = [100-i for i in range(100)]
        self.output_design('100 элементов', solution, medium_inp)

        maximum_inp = [(5000-i)//5 for i in range(5000)]
        self.output_design('5000 элементов', solution, maximum_inp)


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(current_dir, '..', 'src')
    sys.path.insert(0, src_dir)

    from main import solution
    unittest.main()