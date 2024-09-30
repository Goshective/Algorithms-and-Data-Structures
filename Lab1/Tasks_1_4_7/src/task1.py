def insertion_sort(n, lst):
    if n <= 1: return

    for i in range(1, n):
        key_elem = lst[i]
        j = i - 1

        while j >= 0 and key_elem < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key_elem
    return

def main():
    with open('input.txt', 'r') as inp, open('output.txt', 'w') as out:
        n = int(inp.readline())
        lst = [int(x) for x in inp.readline().split()]
        insertion_sort(n, lst)
        print(*lst, file=out, end='')

if __name__ == "__main__":
    main()