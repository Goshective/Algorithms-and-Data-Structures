import os
import sys


PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab7.utils import read_2_n_lst_file, write_file
    

def solution(seq1, seq2):
    n, m = len(seq1), len(seq2)
    cache = []

    def LargestCommonSequence(i, j): # ends on indices i and j for seq1 and seq2
        nonlocal cache
        if cache[i][j] is not None:
            return cache[i][j]
        
        if i == 0 or j == 0:
            cache[i][j] = (0, 0, 0)
            return cache[i][j]
        
        res1, last_i_1, last_j_1 = LargestCommonSequence(i-1, j)
        res2, last_i_2, last_j_2 = LargestCommonSequence(i, j-1)

        el1 = seq1[i]
        new_last_j = None

        for j1 in range(last_j_1 + 1, m):
            if seq2[j1] == el1:
                new_last_j = j1
                break

        el2 = seq2[j]
        new_last_i = None

        for i2 in range(last_i_2 + 1, n):
            if seq1[i2] == el2:
                new_last_i = i2
                break
        
        if new_last_i is None and new_last_j is None:
            if res1 >= res2:
                return res1, last_i_1, last_j_1
            return res2, last_i_2, last_j_2
        
        elif new_last_i is not None and new_last_j is not None:
            if res1 >= res2:
                return res1 + 1, new_last_i, j
            return res2 + 1, i, new_last_j
        
        elif new_last_i is not None:
            return res1 + 1, new_last_i, j
        
        return res2 + 1, i, new_last_j


    for _ in range(n):
        cache.append([None]*len(seq2))
    ans, _, _ = LargestCommonSequence(len(seq1)-1, len(seq2)-1)
    return ans

def main():
    lst1, lst2 = read_2_n_lst_file(os.path.join(PATH, 'txtf', 'input.txt'))
    res = solution(lst1, lst2)
    write_file(os.path.join(PATH, 'txtf', 'output.txt'), res)


if __name__ == "__main__":
    main()