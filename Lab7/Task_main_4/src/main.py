import os
import sys


PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab7.utils import read_2_n_lst_file, write_file


def LargestCommonSequence(i, j): # ends on indices i and j for seq1 and seq2
    global cache
    if cache[i][j] is not None:
        return cache[i][j]
    

def solution(seq1, seq2):
    global cache
    cache = []
    for _ in range(len(seq1)):
        cache.append([None]*len(seq2))
    ans = LargestCommonSequence(len(seq1)-1, len(seq2)-1)
    return ans

def main():
    lst1, lst2 = read_2_n_lst_file(os.path.join(PATH, 'txtf', 'input.txt'))
    res = solution(lst1, lst2)
    write_file(os.path.join(PATH, 'txtf', 'output.txt'), res)


if __name__ == "__main__":
    main()