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

def main(cur_dir):
    n, lst = read_len_lst_file(os.path.join(cur_dir, 'input.txt'), int)
    insertion_sort(n, lst)
    write_lst_file(os.path.join(cur_dir, 'output.txt'), lst)


if __name__ == "__main__":
    import os
    import sys
    
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    common_dir = os.path.join(cur_dir, '..', '..', '..')
    sys.path.insert(0, common_dir)

    from utils import read_len_lst_file, write_lst_file
    main(cur_dir)