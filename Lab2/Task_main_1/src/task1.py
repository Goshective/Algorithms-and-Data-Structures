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

def main(cur_dir):
    n, lst = read_len_lst_file(os.path.join(cur_dir, 'input.txt'), int)
    merge_sort(lst, 0, n - 1)
    write_lst_file(os.path.join(cur_dir, 'output.txt'), lst)


if __name__ == "__main__":
    import os
    import sys
    
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    common_dir = os.path.join(cur_dir, '..', '..', '..')
    sys.path.insert(0, common_dir)

    from utils import read_len_lst_file, write_lst_file
    main(cur_dir)