def bin_search(n, lst, x):
    low, mid, high = 0, 0, n - 1
 
    while low <= high:
        mid = (high + low) // 2
        if lst[mid] < x:
            low = mid + 1
        elif lst[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


def bin_search_loop(n, lst, values):
    res = []
    for v in values:
        res.append(bin_search(n, lst, v))
    return res

def main():
    # path = 'C:/dev/ITMO Education/AnDS/Algorithms-and-Data-Structures/Lab2/Tasks_1_4_6/src/'
    with open('input.txt', 'r') as inp, open('output.txt', 'w') as out:
        n = int(inp.readline())
        lst = [int(x) for x in inp.readline().split()]
        _ = int(inp.readline())
        values = [int(x) for x in inp.readline().split()]
        ans = bin_search_loop(n, lst, values)
        print(*ans, file=out, end='')

if __name__ == "__main__":
    main()