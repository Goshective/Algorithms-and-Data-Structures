import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab2.utils import read_double_len_lst_file, write_lst_file


def bin_search(n, lst, x):
    low, mid, high = 0, 0, n - 1
 
    while low <= high:
        mid = (high + low) // 2
        if lst[mid] < x:
            low = mid + 1
        elif lst[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def bin_search_loop(n, lst, values):
    res = []
    for v in values:
        res.append(bin_search(n, lst, v))
    return res

def main():
    n, lst, _, values = read_double_len_lst_file(os.path.join(PATH, 'txtf', 'input.txt'), int)
    write_lst_file(os.path.join(PATH, 'txtf', 'output.txt'), bin_search_loop(n, lst, values))


if __name__ == "__main__":
    main()