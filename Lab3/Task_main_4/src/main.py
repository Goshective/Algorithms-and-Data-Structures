from bisect import bisect_left
import os
import sys

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PATH, '..', '..'))

from Lab3.utils import read_multi_lst_file, write_lst_file


def segments_parser(lst):
    segments = []
    for l, r in lst:
        segments.append([l, 1])
        segments.append([r, -1])
    return segments

def solution(s, p, lst, points):
    ans = []
    segments = segments_parser(lst)
    segments.sort() # qsort
    segments_for_search = []

    c = 0
    for i in range(2*s):
        x, side = segments[i]
        segments_for_search.append(x)

        segments[i].append(c)
        c += side

    for pt in points:
        idx = bisect_left(segments_for_search, pt)

        if idx == 2*s or pt < segments[0][0]:
            ans.append(0)
        elif pt == segments[idx][0]:
            ans.append(segments[idx][2] + (1 if segments[idx][1] == -1 else 0))
        else:
            ans.append(segments[idx][2])

    return ans

def main():
    (s, p), segments, points = read_multi_lst_file(os.path.join(PATH, 'txtf', 'input.txt'), True)
    ans = solution(s, p, segments, points)
    write_lst_file(os.path.join(PATH, 'txtf', 'output.txt'), ans)


if __name__ == "__main__":
    main()