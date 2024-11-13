import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab1.utils import read_len_lst_file, write_lst_file


def reverse_insertion_sort(n, lst):
    if n <= 1: return

    for i in range(n-2, -1, -1):
        key_elem = lst[i]
        j = i + 1

        while j <= n-1 and key_elem < lst[j]:
            lst[j-1] = lst[j] # swap
            j += 1
        lst[j-1] = key_elem
    return

def main():
    n, lst = read_len_lst_file(os.path.join(PATH, 'txtf', 'input.txt'), int)
    reverse_insertion_sort(n, lst)
    write_lst_file(os.path.join(PATH, 'txtf', 'output.txt'), lst)


if __name__ == "__main__":
    main()