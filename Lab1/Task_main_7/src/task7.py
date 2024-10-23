import os
import sys

def insertion_sort(n, inp_lst):
    lst = [(i, x) for i, x in enumerate(inp_lst)]
    if n <= 1: return lst
    for i in range(1, n):
        key_elem = lst[i]
        j = i - 1
        while j >= 0 and key_elem[1] < lst[j][1]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key_elem
    return lst

def find_info(n, lst):
    s_lst = insertion_sort(n, lst)
    maxi, mini, mid = s_lst[-1][0], s_lst[0][0], s_lst[n//2][0]
    return mini+1, mid+1, maxi+1

def main(cur_dir):
    n, lst = read_len_lst_file(os.path.join(cur_dir, 'input.txt'), int)
    write_lst_file(os.path.join(cur_dir, 'output.txt'), find_info(n, lst))


if __name__ == "__main__":
    import os
    import sys
    
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    common_dir = os.path.join(cur_dir, '..', '..', '..')
    sys.path.insert(0, common_dir)

    from utils import read_len_lst_file, write_lst_file
    main(cur_dir)