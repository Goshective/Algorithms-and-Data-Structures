import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab5.utils import read_n_lst, write_mat_by_lines_file


class Node:
    def __init__(self, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent


def left(i): # 0 -> 1
    return 2 * (i+1) - 1

def right(i): # 0 -> 2
    return 2 * (i+1)

def MinHeapify(lst, i):
    swaps = []
    while True:
        _l = left(i)
        r = right(i)
        if _l > r:
            break
        if _l < len(lst) and lst[_l] < lst[i]:
            largest = _l
        else:
            largest = i

        if r < len(lst) and lst[r] < lst[largest]:
            largest = r

        if largest != i:
            lst[i], lst[largest] = lst[largest], lst[i]
            swaps.append((i, largest))
            i = largest
        else:
            break

    return swaps


def BuildMinHeap(lst):
    heap_size = len(lst)
    swaps = []
    for i in range(heap_size//2, -1, -1):
        swaps += MinHeapify(lst, i)

    return swaps


def solution(lst):
    return BuildMinHeap(lst)


def main():
    _, lst = read_n_lst(os.path.join(PATH, 'txtf', 'input.txt'))
    res = solution(lst)
    out = [[len(res)]] + res
    write_mat_by_lines_file(os.path.join(PATH, 'txtf', 'output.txt'), out)


if __name__ == "__main__":
    main()