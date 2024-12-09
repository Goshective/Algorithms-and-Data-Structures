import os
import sys
from bisect import bisect_left

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PATH, '..', '..'))

from Lab7.utils import read_n_lst_file, write_n_lst_file


def solution(lst):
    n = len(lst)

    tails = []
    indices = []
    prev = [-1]*n

    for i in range(n):
        idx = bisect_left(tails, lst[i])

        if idx == len(tails):
            indices.append(i)
            tails.append(lst[i])
        else:
            indices[idx] = i
            tails[idx] = lst[i]

        if idx > 0:
            prev[i] = indices[idx - 1]

    lis = []
    cur_idx = indices[-1]
    while cur_idx != -1:
        lis.append(lst[cur_idx])
        cur_idx = prev[cur_idx]
    
    lis.reverse()
    return lis


def main():
    lst = read_n_lst_file(os.path.join(PATH, 'txtf', 'input.txt'))
    res = solution(lst)
    write_n_lst_file(os.path.join(PATH, 'txtf', 'output.txt'), len(res), res)


if __name__ == "__main__":
    main()