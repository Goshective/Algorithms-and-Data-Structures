def solution(n): # reverse qsort
    if n <= 1:
        return list(range(1, n+1))
    lst = list(range(n))
    r = n-1
    indices = []

    while 2 <= r:
        mid = r // 2 # l = 0
        indices.append(lst[mid])
        lst[r], lst[mid] = lst[mid], lst[r]
        r -= 1
    
    ans = [0]*n
    for n, idx in enumerate(lst):
        ans[idx] = n+1
    return ans

def main(cur_dir):
    n = read_file(os.path.join(cur_dir, 'input.txt'), int)[0]
    write_lst_file(os.path.join(cur_dir, 'output.txt'), solution(n))


if __name__ == "__main__":
    import os
    import sys
    
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(cur_dir, '..', '..', '..'))

    from utils import read_file, write_lst_file

    main(cur_dir)


