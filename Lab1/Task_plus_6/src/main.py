import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab1.utils import read_len_lst_file, write_lst_file


def bubble_sort(n, lst):
    if n <= 1: return

    for i in range(1, n):
        for j in range(n-1, i-1, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
    return

def main():
    n, lst = read_len_lst_file(os.path.join(PATH, 'input.txt'), int)
    bubble_sort(n, lst)
    write_lst_file(os.path.join(PATH, 'output.txt'), lst)


if __name__ == "__main__":
    main()