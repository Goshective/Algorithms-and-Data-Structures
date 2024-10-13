def find_max_subarray():
    pass


def main():
    with open('input2.txt', 'r') as inp, open('output.txt', 'w') as out:
        n = int(inp.readline())
        lst = [int(x) for x in inp.readline().split()]
        _ = int(inp.readline())
        values = [int(x) for x in inp.readline().split()]
        ans = bin_search_loop(n, lst, values)
        print(*ans, file=out, end='')

if __name__ == "__main__":
    main()