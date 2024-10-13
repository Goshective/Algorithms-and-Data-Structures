

def main():
    with open('input.txt', 'r') as inp, open('output.txt', 'w') as out:
        n = int(inp.readline())
        a = [int(x) for x in inp.readline().split()]
        b = [int(x) for x in inp.readline().split()]
        res = multiply_polynoms(n, a[::-1], b[::-1])
        if res[-1] == 0:
            res.pop()
        print(*res[::-1], file=out, end='')
    return

if __name__ == "__main__":
    main()