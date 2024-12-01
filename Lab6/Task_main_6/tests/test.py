import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))


from Lab6.Task_main_6.src.main import solution

from test_utils import (ConsoleTimeMemory as TM, MB)


class TestHeapSort(unittest.TestCase):
    def test_should_sort_example(self):
        # given

        inp = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8"]
        expected_res = ['Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes']

        # when

        res = solution(inp)

        # then

        self.assertEqual(res, expected_res)

    def check_time_memory_limit(self, res_time, res_memory):
        # given

        expected_memory = 128 * MB
        expected_time = 2

        # when
        # then

        self.assertLessEqual(res_time, expected_time)
        self.assertLessEqual(res_memory, expected_memory)
    
    def test_should_fit_time_memory_limit(self):
        # given
        test_data = [('100 элементов', [f'{1000*i}' for i in range(1, 100)]),
                     ('10e6 элементов', [f'{1000*i}' for i in range(1, 10**6)]),
                     ('5000 разрядов', [f'{i%100}'*50 for i in range(10, 100)])]

        for test_name, input_by_size in test_data:
            # when
            res_time = TM.count_time(solution, input_by_size)
            res_memory = TM.count_memory(solution, input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)


if __name__ == "__main__":
    unittest.main()