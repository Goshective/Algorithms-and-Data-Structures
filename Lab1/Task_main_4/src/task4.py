import os
import sys

def linear_search(lst, v):
    return [i for i, a in enumerate(lst) if a == v]


def main():
    with open('input.txt', 'r') as inp, open('output.txt', 'w') as out:
        lst = [int(x) for x in inp.readline().split()]
        v = int(inp.readline())
        res = linear_search(lst, v)
        if res:
            print(len(res), file=out)
            print(*res, file=out, sep=', ', end='')
        else:
            print(-1, file=out, end='')

def main(cur_dir):
    lst, v = read_file(os.path.join(cur_dir, 'input.txt'), 
                       lambda x: [int(i) for i in x.split()], 
                       int
                       )
    res = linear_search(lst, v)
    ans = f'{len(res)}\n{", ".join(map(str, res))}' if res else -1
    write_file(os.path.join(cur_dir, 'output.txt'), ans)


if __name__ == "__main__":
    import os
    import sys
    
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    common_dir = os.path.join(cur_dir, '..', '..', '..')
    sys.path.insert(0, common_dir)

    from utils import read_file, write_file
    main(cur_dir)