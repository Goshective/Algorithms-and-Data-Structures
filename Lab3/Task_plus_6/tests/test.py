import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab3.Task_plus_6.src.main import (
    solution, 
    qsort,
    radix_sort,
    )
from test_utils import (
    ConsoleTimeMemory as TM, 
    get_task_name,
    MB
)


class TestCaseMultiArray(unittest.TestCase):
    def test_should_sort(self):
        # given
        a, b = [7, 1, 4, 9], [2, 7, 8, 11]
        expected_res = 51

        # when
        res = solution(len(a), len(b), a, b, qsort)
        
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

        for func_name, func in ('Quick sort (Python):', qsort), ('Radix sort:', radix_sort):
            # given
            test_data = [(f'{i}^2 элементов', (i, i, list(range(i, 0, -1)), list(range(i, 0, -1)), func)) 
                            for i in (4, 500, 1000)]

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