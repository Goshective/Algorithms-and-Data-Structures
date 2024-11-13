import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab1.utils import read_lst_value_file, write_line_lst_line_file, write_file

def linear_search(lst, v):
    return [i for i, a in enumerate(lst) if a == v]


def main():
    with open('input.txt', 'r') as inp, open('output.txt', 'w') as out:
        lst = [int(x) for x in inp.readline().split()]
        v = int(inp.readline())
        res = linear_search(lst, v)
        if res:
            print(len(res), file=out)
            print(*res, file=out, sep=', ', end='')
        else:
            print(-1, file=out, end='')

def main():
    lst, v = read_lst_value_file(os.path.join(PATH, 'txtf', 'input.txt'), int)
    res = linear_search(lst, v)
    out_path = os.path.join(PATH, 'txtf', 'output.txt')
    if res:
        write_line_lst_line_file(out_path, len(res), res, sep=', ')
    else:
        write_file(out_path, -1)


if __name__ == "__main__":
    main()