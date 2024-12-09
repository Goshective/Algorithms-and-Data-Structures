import os
import sys

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PATH, '..', '..'))

from Lab1.utils import read_len_lst_file, write_lst_file


def insertion_sort(n, inp_lst):
    lst = [(i, x) for i, x in enumerate(inp_lst)]
    if n <= 1: return lst
    for i in range(1, n):
        key_elem = lst[i]
        j = i - 1
        while j >= 0 and key_elem[1] < lst[j][1]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key_elem
    return lst

def find_info(n, lst):
    s_lst = insertion_sort(n, lst)
    maxi, mini, mid = s_lst[-1][0], s_lst[0][0], s_lst[n//2][0]
    return mini+1, mid+1, maxi+1

def main():
    n, lst = read_len_lst_file(os.path.join(PATH, 'txtf', 'input.txt'), int)
    write_lst_file(os.path.join(PATH, 'txtf', 'output.txt'), find_info(n, lst))


if __name__ == "__main__":
    main()