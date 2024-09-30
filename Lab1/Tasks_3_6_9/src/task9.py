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


def main():
    with open('input.txt', 'r') as inp, open('output.txt', 'w') as out:
        a, b = [[int(x) for x in st] for st in inp.readline().rstrip().split()]
        res = bin_sum(a, b)
        print(*res, file=out, sep='', end='')


if __name__ == "__main__":
    main()