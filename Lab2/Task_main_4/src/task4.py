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

def main(cur_dir):
    n, lst, _, values = read_file(os.path.join(cur_dir, 'input.txt'), 
                       int, 
                       lambda x: [int(i) for i in x.split()],
                       int, 
                       lambda x: [int(i) for i in x.split()]
                       )
    write_lst_file(os.path.join(cur_dir, 'output.txt'), bin_search_loop(n, lst, values))


if __name__ == "__main__":
    import os
    import sys
    
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    common_dir = os.path.join(cur_dir, '..', '..', '..')
    sys.path.insert(0, common_dir)

    from utils import read_file, write_lst_file
    main(cur_dir)