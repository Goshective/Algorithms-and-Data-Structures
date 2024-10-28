import heapq
import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab3.utils import read_file, write_file


def cross_multiplication(a, b):
    res = []
    for i in a:
        for j in b:
            res.append(i * j)
    return res

def radix_sort(lst):
    freq = [0]*40001
    for i in lst:
        freq[i] += 1
    ans = []
    for n in range(40001):
        if n != 0:
            ans += [n]*freq[n]
    lst[:] = ans

def qsort(lst):
    lst.sort()

def heap_algo(n, m, a, b):
    heap = []
    result = []
    visited = set()

    heapq.heappush(heap, (a[0] * b[0], 0, 0))
    visited.add((0, 0))
    
    while len(result) < n * m:
        product, i, j = heapq.heappop(heap)
        result.append(product)
        
        if i + 1 < n and (i + 1, j) not in visited: # Push next pairs
            heapq.heappush(heap, (a[i + 1] * b[j], i + 1, j))
            visited.add((i + 1, j))
        
        if j + 1 < m and (i, j + 1) not in visited:
            heapq.heappush(heap, (a[i] * b[j + 1], i, j + 1))
            visited.add((i, j + 1))

    return result

def solution(n, m, a, b, sort_func):
    sort_func(a)
    sort_func(b)
    res_arr = heap_algo(n, m, a, b)
    return sum(res_arr[i] for i in range(0, n*m, 10))

def main():
    (n, m), a, b = read_file(os.path.join(PATH, 'txtf', 'input.txt'), 
                           lambda x: map(int, x.split()),
                           lambda x: [int(i) for i in x.split()],
                           lambda x: [int(i) for i in x.split()]
                           )
    res = solution(n, m, a, b, radix_sort)
    write_file(os.path.join(PATH, 'txtf', 'output.txt'), res)


if __name__ == "__main__":
    main()