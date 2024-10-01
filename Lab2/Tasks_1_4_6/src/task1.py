def merge(lst, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0, n1):
        L[i] = lst[l + i]
    for j in range(0, n2):
        R[j] = lst[m + 1 + j]
 
    i, j = 0, 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            lst[k] = L[i]
            i += 1
        else:
            lst[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        lst[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        lst[k] = R[j]
        j += 1
        k += 1
 
def merge_sort(lst, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort(lst, l, m)
        merge_sort(lst, m + 1, r)
        merge(lst, l, m, r)

def main():
    # path = 'C:/dev/ITMO Education/AnDS/Algorithms-and-Data-Structures/Lab2/Tasks_1_4_6/src/'
    with open('input.txt', 'r') as inp, open('output.txt', 'w') as out:
        n = int(inp.readline())
        lst = [int(x) for x in inp.readline().split()]
        merge_sort(lst, 0, n - 1)
        print(*lst, file=out, end='')

if __name__ == "__main__":
    main()