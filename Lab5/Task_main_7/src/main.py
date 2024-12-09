import os
import sys

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PATH, '..', '..'))

from Lab5.utils import read_n_lst, write_lst_file


def left(i):
    return 2 * (i+1) - 1

def right(i):
    return 2 * (i+1)

def MinHeapify(lst, i, heap_size=None):
    if heap_size is None:
        heap_size = len(lst)

    while True:
        _l = left(i)
        r = right(i)
        if _l > r:
            break
        if _l < heap_size and lst[_l] < lst[i]:
            smallest = _l
        else:
            smallest = i

        if r < heap_size and lst[r] < lst[smallest]:
            smallest = r

        if smallest != i:
            lst[i], lst[smallest] = lst[smallest], lst[i]
            i = smallest
        else:
            break

def BuildMinHeap(lst):
    heap_size = len(lst)
    swaps = []
    for i in range(heap_size//2, -1, -1):
        MinHeapify(lst, i)

    return swaps

def HeapSort(lst):
    BuildMinHeap(lst)
    heap_size = len(lst)
    for i in range(len(lst)-1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heap_size = heap_size - 1
        MinHeapify(lst, 0, heap_size)


def solution(lst, sort_func=HeapSort):
    res = lst.copy()
    if sort_func == HeapSort:
        sort_func(res)
    else:
        sort_func(res, 0, len(res)-1)
    return res


def main():
    lst = read_n_lst(os.path.join(PATH, 'txtf', 'input.txt'))[1]
    res = solution(lst)
    write_lst_file(os.path.join(PATH, 'txtf', 'output.txt'), res)


if __name__ == "__main__":
    main()