def bubble_sort(n, lst):
    if n <= 1: return

    for i in range(1, n):
        for j in range(n-1, i-1, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
    return

def main():
    with open('input.txt', 'r') as inp, open('output.txt', 'w') as out:
        n = int(inp.readline())
        lst = [int(x) for x in inp.readline().split()]
        bubble_sort(n, lst)
        print(*lst, file=out, end='')

if __name__ == "__main__":
    main()