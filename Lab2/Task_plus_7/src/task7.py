def find_max_subarray(n, lst):
    prefix_sum = []
    s = 0
    for el in lst:
        s += el
        prefix_sum.append(s)

    min_i = 0
    j = 1
    max_subarr = (0, 0, lst[0])
    while j < n:
        cur_profit = prefix_sum[j] if min_i == 0 else prefix_sum[j] - prefix_sum[min_i]
        if prefix_sum[j] < prefix_sum[min_i]:
            min_i = j
        elif cur_profit > max_subarr[2]:
            max_subarr = ((min_i+1 if min_i != 0 else min_i), j, cur_profit)

        j += 1

    low, high, profit = max_subarr
    return low, high, profit

def diff_array(n, lst):
    return [lst[i] - lst[i-1] for i in range(1, n)]


def solution(n, lst):
    diff_lst = diff_array(n, lst)
    low, high, profit = find_max_subarray(n - 1, diff_lst)
    return low, high + 1, round(profit, 3)

def main(cur_dir):
    n, lst = read_len_lst_file(os.path.join(cur_dir, 'input.txt'), int)
    write_lst_file(os.path.join(cur_dir, 'output.txt'), solution(n, lst))


if __name__ == "__main__":
    import os
    import sys
    
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    common_dir = os.path.join(cur_dir, '..', '..', '..')
    sys.path.insert(0, common_dir)

    from utils import read_len_lst_file, write_lst_file
    main(cur_dir)