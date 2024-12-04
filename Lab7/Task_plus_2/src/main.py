import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab7.utils import read_file, write_n_lst_file



def solution(n):
    stack = [(1, n, 1), (2, n, 1), (3, n, 1)]
    best_res = []
    cur_res = []
    prev_depth = 0

    if n == 1: return [1]

    while stack:
        operation, num, depth = stack.pop()
        if num % operation != 0:
            continue

        new_num = num - 1 if operation == 1 else num // operation

        if depth <= prev_depth:
            # moving from layers of solution
            for _ in range(prev_depth - depth + 1):
                cur_res.pop()

        cur_res.append(new_num)
        prev_depth = depth

        if new_num == 1:
            if len(cur_res) < len(best_res) or len(best_res) == 0:
                best_res = cur_res.copy()
            continue
        elif len(cur_res) >= len(best_res) and len(best_res) != 0:
            continue

        for op in (1, 2, 3):
            stack.append((op, new_num, depth + 1))

    ans = best_res[::-1] + [n]

    return ans

def main():
    n = read_file(os.path.join(PATH, 'txtf', 'input.txt'), int)[0]
    res = solution(n)
    k = len(res) - 1
    write_n_lst_file(os.path.join(PATH, 'txtf', 'output.txt'), k, res)


if __name__ == "__main__":
    main()