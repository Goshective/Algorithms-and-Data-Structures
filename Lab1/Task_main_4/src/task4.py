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


if __name__ == "__main__":
    main()