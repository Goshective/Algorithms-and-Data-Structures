import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))


from Lab7.Task_main_4.src.main import solution

from test_utils import (
    ConsoleTimeMemory as TM, 
    get_task_name,
    MB
)


class TestLCS(unittest.TestCase):
    def test_should_find_full_sequence(self):
        # given

        inp = ([2, 7, 5],
               [2, 5])
        expected_res = 2

        # when

        res = solution(*inp)

        # then

        self.assertEqual(res, expected_res)

    def test_should_find_mixed_sequence(self):
        # given

        inp = ([2, 7, 8, 3],
               [5, 2, 8, 7])
        expected_res = 2

        # when

        res = solution(*inp)

        # then

        self.assertEqual(res, expected_res)

    def test_should_not_find_any_subsequence(self):
        # given

        inp = ([7],
               [1, 2, 3, 4])
        expected_res = 0

        # when

        res = solution(*inp)

        # then

        self.assertEqual(res, expected_res)

    def test_should_find_hidden_subsequence(self):
        # given

        inp = ([1, 2, 3, 4, 0, 5, 0, 6, 0, 7],
               [5, 1, 6, 2, 7, 3, 4])
        expected_res = 4

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
        for n in (10, 50, 100):
            data = ([i for i in range(n // 2)], [2*i for i in range(n // 2)])
            test_data.append((f'{n} элементов', data))

        print()
        print('-'*55)
        print(get_task_name(PATH))

        for test_name, input_by_size in test_data:
            # when
            res_time = TM.count_time(solution, *input_by_size)
            res_memory = TM.count_memory(solution, *input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)

        print('-'*55)


if __name__ == "__main__":
    unittest.main()