import os
import sys

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PATH, '..', '..'))

from Lab4.utils import read_commands, write_lst_by_lines_file


def solution(lst):
    stack = []
    ans = []
    for command in lst:
        cmd = command.split()
        if cmd[0] == '+':
            stack.append(int(cmd[1]))
        else:
            ret = stack.pop()
            ans.append(ret)
    return ans

def main():
    lst = read_commands(os.path.join(PATH, 'txtf', 'input.txt'))
    res = solution(lst)
    write_lst_by_lines_file(os.path.join(PATH, 'txtf', 'output.txt'), res)


if __name__ == "__main__":
    main()