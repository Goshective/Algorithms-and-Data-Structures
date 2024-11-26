import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab4.Task_plus_12.src.main import solution
from test_utils import (ConsoleTimeMemory as TM, MB)


class TestsLinkedDict(unittest.TestCase):
    def test_should_find_1_neighbour(self):
        # given
        inp = 3, [
            'left 2 1',
            'right 3 1',
            'name 1']
        expected_res = [[2, 3]]

        # when
        res = solution(*inp)

        # then
        self.assertEqual(res, expected_res)

    def test_should_work_as_queue_mid(self):
        # given
        inp = 3, [
            'left 2 1',
            'leave 1',
            'right 3 1',
            'name 1']
        expected_res = [[0, 3]]

        # when
        res = solution(*inp)

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
        # given
        test_data = []
        for k in (100, 1000, 75000):
            commands_list = [f'left {i} {i+2}' for i in range(1, k//4 - 1, 2)]
            commands_list += [f'right {i} {i-1}' for i in range(2, k//4, 2)]
            for i in range(1, k//4):
                commands_list += [f'name {i}'] + [f'leave {i}']
            
            test_data.append((f'{k} элементов', (k, commands_list)))

        for test_name, input_by_size in test_data:
            # when
            res_time = TM.count_time(solution, *input_by_size)
            res_memory = TM.count_memory(solution, *input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)


if __name__ == "__main__":
    unittest.main()