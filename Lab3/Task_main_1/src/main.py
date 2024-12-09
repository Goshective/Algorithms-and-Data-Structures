from random import randint
import os
import sys

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PATH, '..', '..'))

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

def Partition3(A, l, r):
    x = A[l]
    i = l + 1
     
    m2 = 1
    for j in range(l + 1, r + 1):
        if A[j] <= x:
            if A[j] == x:
                m2 += 1
            A[i], A[j] = A[j], A[i]
            i += 1

    p = i - 1
    k = l
    c = 0
    while k < p:
        if A[k] != x:
            k += 1
            continue
        while p > k and A[p] == x:
            p -= 1
        
        A[k] , A[p] = A[p] , A[k]
        k += 1
        c += 1
        if c == m2:
            break
    m1 = p 
    m2 += m1 - 1
    return m1, m2

def RandomizedQuickSort3(A, l, r):
    if l < r:
        k = randint(l, r)
        A[l], A[k] = A[k], A[l]
        m1, m2 = Partition3(A, l, r)

        RandomizedQuickSort3(A, l, m1 - 1)
        RandomizedQuickSort3(A, m2 + 1, r)

def main():
    n, lst = read_len_lst_file(os.path.join(PATH, 'txtf', 'input.txt'), int)
    RandomizedQuickSort3(lst, 0, n-1)
    write_lst_file(os.path.join(PATH, 'txtf', 'output.txt'), lst)


if __name__ == "__main__":
    main()