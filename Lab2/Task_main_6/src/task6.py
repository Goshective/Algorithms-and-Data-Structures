def find_max_crossing_subarray(lst, low, mid, high):
    left_sum = lst[mid]-1
    s = 0
    for i in range(mid, low-1, -1):
        s += lst[i]
        if s > left_sum:
            left_sum = s
            maxleft = i
    right_sum = lst[mid+1]-1
    s = 0
    for j in range(mid+1, high+1):
        s += lst[j]
        if s > right_sum:
            right_sum = s
            maxright = j
    return maxleft, maxright, left_sum + right_sum

def find_max_subarray(lst, low, high):
    if high == low:
        return low, high, lst[low]
    
    mid = (low + high) // 2
    left_low, left_high, left_sum = find_max_subarray(lst, low, mid)
    right_low, right_high, right_sum = find_max_subarray(lst, mid+1, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(lst, low, mid, high)
    if left_sum >= max(right_sum, cross_sum):
        return left_low, left_high, left_sum
    elif right_sum >= max(left_sum, cross_sum):
        return right_low, right_high, right_sum
    return cross_low, cross_high, cross_sum

def diff_array(n, lst):
    return [lst[i] - lst[i-1] for i in range(1, n)]


def solution(n, lst):
    diff_lst = diff_array(n, lst)
    low, high, profit = find_max_subarray(diff_lst, 0, (n - 1)-1)
    return low, high + 1, round(profit, 3)

def main(cur_dir):
    lst = read_file(os.path.join(cur_dir, 'input.txt'), 
                       lambda x: [float(i) for i in x.split()]
                       )[0]
    res = solution(len(lst), lst)
    ans = " ".join(map(str, res)) + '\n' + \
    f'Buy: for {lst[res[0]]} at {res[0]}, Sell: for {lst[res[1]]} at {res[1]}. Profit: {res[2]}'
    write_file(os.path.join(cur_dir, 'output.txt'), ans)


if __name__ == "__main__":
    import os
    import sys
    
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    common_dir = os.path.join(cur_dir, '..', '..', '..')
    sys.path.insert(0, common_dir)

    from utils import read_file, write_file
    main(cur_dir)