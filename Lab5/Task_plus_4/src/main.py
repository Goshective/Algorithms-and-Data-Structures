import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab5.utils import read_n_lst, write_mat_by_lines_file


class Node:
    pass


class Heap:
    pass


def min_heap():
    pass


def solution(lst):
    queue = 2
    ans = []
    for command in lst:
        cmd = command.split()
        if cmd[0] == '+':
            queue.put(Node(int(cmd[1])))
        elif cmd[0] == '*':
            queue.put_to_mid(Node(int(cmd[1])))
        else:
            ret = queue.get()
            ans.append(ret.val)
        # queue.print()
    return ans

def main():
    _, lst = read_n_lst(os.path.join(PATH, 'txtf', 'input.txt'))
    res = solution(lst)
    write_mat_by_lines_file(os.path.join(PATH, 'txtf', 'output.txt'), res)


if __name__ == "__main__":
    main()