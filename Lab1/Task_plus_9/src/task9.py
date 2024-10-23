def bin_sum(a, b):
    ret = []
    carry = 0
    for i in range(len(a)-1, -1, -1):
        if a[i] == 1 and b[i] == 1:
            ret.append(1 if carry == 1 else 0)
            carry = 1
        elif a[i] == 0 and b[i] == 0:
            ret.append(1 if carry == 1 else 0)
            carry = 0
        else:
            ret.append(0 if carry == 1 else 1)
    if carry == 1:
        ret.append(1)
    return ret[::-1]

def main(cur_dir):
    a, b = read_file(os.path.join(cur_dir, 'input.txt'), 
                       lambda line: [[int(x) for x in st] for st in line.split()]
                       )[0]
    res = bin_sum(a, b)
    write_file(os.path.join(cur_dir, 'output.txt'), "".join(map(str, res)))


if __name__ == "__main__":
    import os
    import sys

    cur_dir = os.path.dirname(os.path.abspath(__file__))
    common_dir = os.path.join(cur_dir, '..', '..', '..')
    sys.path.insert(0, common_dir)

    from utils import read_file, write_file
    main(cur_dir)