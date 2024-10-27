def solution(n, k, points):
    points.sort(key=lambda x: x[0]**2 + x[1]**2)
    return points[:k]

def main(cur_dir):
    with open(os.path.join(cur_dir, 'input.txt'), 'r') as inp:
        n, k = map(int, inp.readline().split())
        points = []
        for _ in range(n):
            points.append([int(x) for x in inp.readline().split()])
    ans = solution(n, k, points)
    print(points, ans)

    with open(os.path.join(cur_dir, 'output.txt'), 'w') as out:
        print(*ans, file=out, sep=',', end='')


if __name__ == "__main__":
    import os
    
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    main(cur_dir)