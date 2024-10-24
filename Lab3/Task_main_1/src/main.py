from random import randint
import os

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

def main(cur_dir):
    n, lst = read_len_lst_file(os.path.join(cur_dir, 'input.txt'), int)
    RandomizedQuickSort(lst, 0, n-1)
    write_lst_file(os.path.join(cur_dir, 'output.txt'), lst)


if __name__ == "__main__":
    import os
    import sys
    
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    common_dir = os.path.join(cur_dir, '..', '..', '..')
    sys.path.insert(0, common_dir)

    from utils import read_len_lst_file, write_lst_file
    main(cur_dir)