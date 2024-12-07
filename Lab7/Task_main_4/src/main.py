import os
import sys


PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab7.utils import read_2_n_lst_file, write_file
    

def solution(seq1, seq2):
    n = len(seq1)
    m = len(seq2)
    
    table = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq1[i - 1] == seq2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    return table[n][m]

def main():
    lst1, lst2 = read_2_n_lst_file(os.path.join(PATH, 'txtf', 'input.txt'))
    res = solution(lst1, lst2)
    write_file(os.path.join(PATH, 'txtf', 'output.txt'), res)


if __name__ == "__main__":
    main()