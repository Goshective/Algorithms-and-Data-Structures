import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab5.Task_plus_2.src.main import solution
from test_utils import (
    ConsoleTimeMemory as TM, 
    get_task_name,
    MB
)


class TestsTreeHeight(unittest.TestCase):
    def test_should_find_simple_height(self):
        # given
        inp = [4, -1, 4, 1, 1]
        expected_res = 3

        # when
        res = solution(inp)

        # then
        self.assertEqual(res, expected_res)

    def test_should_find_height_of_straight_tree(self):
        # given
        inp = [-1, 0, 4, 0, 3]
        expected_res = 4

        # when
        res = solution(inp)

        # then
        self.assertEqual(res, expected_res)

    def test_should_find_height_of_one_node(self):
        # given
        inp = [-1]
        expected_res = 1

        # when
        res = solution(inp)

        # then
        self.assertEqual(res, expected_res)

    def check_time_memory_limit(self, res_time, res_memory):
        # given

        expected_memory = 512 * MB
        expected_time = 3

        # when
        # then
        
        self.assertLessEqual(res_time, expected_time)
        self.assertLessEqual(res_memory, expected_memory)
    
    def test_should_fit_time_memory_limit(self):
        # given
        test_data = [('100 элементов', [-1] + [i // 2 for i in range(100)]),
                     ('10e3 элементов', [-1] + [i // 4 for i in range(1000)]),
                     ('10e5 элементов', [-1] + [i // 8 for i in range(10**5)])]

        
        print()
        print('-'*55)
        print(get_task_name(PATH))

        for test_name, input_by_size in test_data:
            # when
            res_time = TM.count_time(solution, input_by_size)
            res_memory = TM.count_memory(solution, input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)

        print('-'*55)


if __name__ == "__main__":
    unittest.main()