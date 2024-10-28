import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab3.utils import read_lst_file, write_file


def radix_sort(lst):
    freq = [0]*5001
    for i in lst:
        freq[i] += 1
    ans = []
    for n in range(5000, -1, -1):
        if n != 0:
            ans += [n]*freq[n]
    return ans

def solution(citations):
    citations = radix_sort(citations)
    c = 0
    for i in range(len(citations)):
        if citations[i] < c + 1:
            break
        c += 1
    return c

def main():
    lst = read_lst_file(os.path.join(PATH, 'txtf', 'input.txt'), int, sep=',')
    write_file(os.path.join(PATH, 'txtf', 'output.txt'), solution(lst))


if __name__ == "__main__":
    main()