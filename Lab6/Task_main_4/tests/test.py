import unittest
import sys
import os

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))


from Lab6.Task_main_4.src.main import solution

from test_utils import (ConsoleTimeMemory as TM, MB)


class TestHeapSort(unittest.TestCase):
    def test_should_sort_example(self):
        # given

        inp = [
            "put zero a",
            "put one b",
            "put two c",
            "put three d",
            "put four e",
            "get two",
            "prev two",
            "next two",
            "delete one",
            "delete three",
            "get two",
            "prev two",
            "next two",
            "next four"]
        expected_res = ['c', 'b', 'd', 'c', 'a', 'e', '<none>']

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
        # given
        test_data = []
        for title, n in (('100 элементов', 100), ('10e3 элементов', 1000), ('5*10e5 элементов', 5*10**5)):
            data = [f'put {101*i} a' for i in range(n // 2)] + [f'prev {101*i} a' for i in range(n // 4)]
            data += [f'del {101*i} a' for i in range(n // 4)]
            test_data.append((title, data))

        for test_name, input_by_size in test_data:
            # when
            res_time = TM.count_time(solution, input_by_size)
            res_memory = TM.count_memory(solution, input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)


if __name__ == "__main__":
    unittest.main()