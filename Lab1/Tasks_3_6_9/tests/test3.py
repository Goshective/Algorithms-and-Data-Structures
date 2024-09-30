import unittest
import sys
import os
import time
import tracemalloc

class InsertionSortTestCase(unittest.TestCase):
    def output_design(self, test_num, func, ln, lst):
        t_start = time.perf_counter()
        tracemalloc.start()
        func(ln, lst)

        print(f"Тест {test_num}:")
        print("Время работы: %s секунд " % (time.perf_counter() - t_start), end='\n')
        print("Затрачено памяти:", tracemalloc.get_traced_memory()[1], "байт")
        tracemalloc.stop()

    def test_correctness(self):
        inp = [31, 41, 59, 26, 41, 58]
        reverse_insertion_sort(len(inp), inp)
        self.assertEqual(inp, [26, 31, 41, 41, 58, 59][::-1])

        inp = [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]
        reverse_insertion_sort(len(inp), inp)
        self.assertEqual(inp, list(range(9, -1, -1)))
    
    def test_time_memory(self):
        minimum_inp = list(range(9, -1, -1))
        self.output_design(1, reverse_insertion_sort, 10, minimum_inp)
        self.assertEqual(minimum_inp, list(range(9, -1, -1)))

        maximum_inp = list(range(10**3))
        self.output_design(2, reverse_insertion_sort, 10**3, maximum_inp)
        self.assertEqual(maximum_inp, list(range(10**3-1, -1, -1)))
        


if __name__ == "__main__":
    # Get the current directory of the test file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Get the directory of the source file
    src_dir = os.path.join(current_dir, '..', 'src')

    # Add the source directory to the system path
    sys.path.insert(0, src_dir)

    from task3 import reverse_insertion_sort
    unittest.main()