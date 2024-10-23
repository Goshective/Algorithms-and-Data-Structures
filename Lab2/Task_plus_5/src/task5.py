import os
def is_more_than_half(lst, low, high):
    if high == low:
        return True, lst[low]
    if high == low + 1:
        return lst[low] == lst[high], lst[low]
    
    mid = (low + high) // 2
    _, num1 = is_more_than_half(lst, low, mid)
    _, num2 = is_more_than_half(lst, mid+1, high)
    c1, c2 = 0, 0
    for i in range(low, high+1):
        if lst[i] == num1: c1 += 1
        elif lst[i] == num2: c2 += 1
    if num1 == num2:
        return c1 + c2 > (high - low + 1)//2, num1
    if c1 > c2 and c1 > (high - low + 1)//2:
        return True, num1
    if c2 < c1 and c2 > (high - low + 1)//2:
        return True, num2
    return False, num1 if c1 >= c2 else num2


def solution(n, lst):
    return int(is_more_than_half(lst, 0, n-1)[0])

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