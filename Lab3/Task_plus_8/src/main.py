import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab3.utils import read_multi_lst_file, write_lst_file


def solution(_, k, points):
    points.sort(key=lambda x: x[0]**2 + x[1]**2)
    return points[:k]

def main():
    (n, k), points = read_multi_lst_file(os.path.join(PATH, 'txtf', 'input.txt'))
    ans = solution(n, k, points)

    write_lst_file(os.path.join(PATH, 'txtf', 'output.txt'), ans, sep=',')


if __name__ == "__main__":
    main()