def solution(citations):
    citations.sort(reverse=True) # quick-sort
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