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

def main():
    path = os.path.dirname(os.path.abspath(__file__)) + '/'
    with open(path + 'input.txt', 'r') as inp, open(path + 'output.txt', 'w') as out:
        n = int(inp.readline())
        lst = [int(x) for x in inp.readline().split()]
        RandomizedQuickSort(lst, 0, n - 1)
        print(*lst, file=out, end='')

if __name__ == "__main__":
    main()