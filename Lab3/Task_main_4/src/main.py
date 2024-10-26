from bisect import bisect_left

def main(cur_dir):

    with open(os.path.join(cur_dir, 'input.txt'), 'r') as inp:
        s, p = map(int, inp.readline().split())
        segments = []
        for _ in range(s):
            l, r = map(int, inp.readline().split())
            segments.append((l, r))
        points = [int(x) for x in inp.readline().split()]
    ans = solution(s, p, segments, points)

    with open(os.path.join(cur_dir, 'output.txt'), 'w') as out:
        print(*ans, file=out, end='')

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


if __name__ == "__main__":
    import os
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    main(cur_dir)