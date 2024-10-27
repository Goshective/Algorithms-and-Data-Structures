def radix_sort(lst):
    freq = [0]*5001
    for i in lst:
        freq[i] += 1
    ans = []
    for n in range(5000, -1, -1):
        if n != 0:
            ans += [n]*freq[n]
    return ans

def solution(citations):
    citations = radix_sort(citations)
    c = 0
    for i in range(len(citations)):
        if citations[i] < c + 1:
            break
        c += 1
    return c

def main(cur_dir):
    lst = read_file(os.path.join(cur_dir, 'input.txt'), lambda x: [int(i) for i in x.split(',')])[0]
    write_file(os.path.join(cur_dir, 'output.txt'), solution(lst))


if __name__ == "__main__":
    import os
    import sys
    
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(cur_dir, '..', '..', '..'))

    from utils import read_file, write_file

    main(cur_dir)