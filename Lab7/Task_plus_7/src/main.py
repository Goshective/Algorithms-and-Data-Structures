import os
import sys


PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab7.utils import read_file, write_file


def solution(pattern, st):
    n, m = len(st), len(pattern)
    
    dp = [[False] * (m+1) for _ in range(n+1)]
    dp[0][0] = True

    for j in range(1, m + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pattern[j-1] == '?' or pattern[j-1] == st[i-1]:
                dp[i][j] = dp[i-1][j-1]
            elif pattern[j-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]

    return "YES" if dp[n][m] else "NO"


def main():
    pattern, st = read_file(os.path.join(PATH, 'txtf', 'input.txt'), str, str)
    res = solution(pattern, st)
    write_file(os.path.join(PATH, 'txtf', 'output.txt'), res)


if __name__ == "__main__":
    main()