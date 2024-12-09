import unittest
import sys
import os
from random import shuffle

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab2.Task_main_1.src.main import merge_sort
from Lab3.Task_main_1.src.main import RandomizedQuickSort
from Lab5.Task_main_7.src.main import solution, HeapSort

from test_utils import (
    ConsoleTimeMemory as TM, 
    get_task_name,
    MB
)


class TestHeapSort(unittest.TestCase):
    def test_should_sort_example(self):
        # given

        inp = [31, 41, 59, 26, 41, 58]
        expected_res = [26, 31, 41, 41, 58, 59][::-1]

        # when

        res = solution(inp)

        # then

        self.assertEqual(res, expected_res)

    def test_should_sort_growing_sequence(self):
        # given

        inp = [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]
        expected_res = list(range(9, -1, -1))

        # when

        res = solution(inp)

        # then

        self.assertEqual(res, expected_res)

    def check_time_memory_limit(self, res_time, res_memory):
        # given

        expected_memory = 256 * MB
        expected_time = 2

        # when
        # then

        self.assertLessEqual(res_time, expected_time)
        self.assertLessEqual(res_memory, expected_memory)
    
    def test_should_fit_time_memory_limit(self):
        print()
        print('-'*55)
        print(get_task_name(PATH))

        for func_name, func in (('Merge sort:', merge_sort), 
                                ('Randomized Quick sort:', RandomizedQuickSort), 
                                ('Heap sort:', HeapSort)):
            # given
            test_data = []
            for i in (10**3, 10**4, 10**5):
                inp_lst = [(10**4 * i)*(-1)**(i%2) for i in range(i)]
                shuffle(inp_lst)
                test_data.append((f'{i} элементов', (inp_lst, func)))

            for test_id, (test_name, input_by_size) in enumerate(test_data):
                # when
                res_time = TM.count_time(solution, *input_by_size)
                res_memory = TM.count_memory(solution, *input_by_size)

                if test_id == 0:
                    print()
                    print(func_name)
                TM.output_design(test_name, res_time, res_memory)

                # then
                self.check_time_memory_limit(res_time, res_memory)

        print('-'*55)


if __name__ == "__main__":
    unittest.main()