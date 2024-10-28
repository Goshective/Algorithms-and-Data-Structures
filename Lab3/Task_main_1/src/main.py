from random import randint
import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
# LEFT_IDX = 0
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab3.utils import read_len_lst_file, write_lst_file


def Partition(A,l,r):
    x = A[l]
    j = l
    for i in range(l + 1, r + 1):
        if A[i] <= x:
            j += 1
            A[j], A[i] = A[i], A[j]
    A[l], A[j] = A[j], A[l]
    return j

def RandomizedQuickSort(A, l, r):
    if l < r:
        k = randint(l, r)
        A[l], A[k] = A[k], A[l]
        m = Partition(A, l, r)
        RandomizedQuickSort(A, l, m - 1)
        RandomizedQuickSort(A, m + 1, r)
    return

def main():
    n, lst = read_len_lst_file(os.path.join(PATH, 'txtf', 'input.txt'), int)
    RandomizedQuickSort(lst, 0, n-1)
    write_lst_file(os.path.join(PATH, 'txtf', 'output.txt'), lst)


if __name__ == "__main__":
    main()