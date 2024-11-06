from random import randint
import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab4.utils import read_multiple_string_file, write_lst_by_lines_file


def solution(lst):
    stack = []
    ans = []
    for command, i in lst:
        if i is not None:
            stack.append(i)
        else:
            ret = stack.pop()
            ans.append(ret)
    return ans

def main():
    n, lst = read_multiple_string_file(os.path.join(PATH, 'txtf', 'input.txt'))
    res = solution(lst)
    write_lst_by_lines_file(os.path.join(PATH, 'txtf', 'output.txt'), res)


if __name__ == "__main__":
    main()