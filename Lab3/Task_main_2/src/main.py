# def main(cur_dir):
#     n, lst = read_len_lst_file(os.path.join(cur_dir, 'input.txt'), int)
#     RandomizedQuickSort(lst, 0, n-1)
#     write_lst_file(os.path.join(cur_dir, 'output.txt'), lst)

def qsort (left, right):
    global c
    key = a [(left + right) // 2]
    i = left
    j = right
    while i <= j:
        while a[i] < key: # first while
            i += 1
            c += 1
        while a[j] > key : # second while
            j -= 1
            c += 1
        if i <= j :
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
            c += 2
        print(a, key)
    if left < j:
        qsort(left, j)
    if i < right:
        qsort(i, right)

def reverse_qsort(left, right):
    pass

if __name__ == "__main__":
    import os
    import sys
    
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    common_dir = os.path.join(cur_dir, '..', '..', '..')
    sys.path.insert(0, common_dir)
    c = 0

    from utils import read_len_lst_file, write_lst_file
    a = [2, 4, 1, 3]
    print(a)
    # main(cur_dir)
    qsort(0, len(a) - 1)
    print(c)


