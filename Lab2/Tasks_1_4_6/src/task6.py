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
    return maxleft, maxright, left_sum - right_sum

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


def main():
    with open('input2.txt', 'r') as inp, open('output.txt', 'w') as out:
        lst = [float(x) for x in inp.readline().split()]
        ans = find_max_subarray(lst, 0, len(lst)-1)
        print(*ans, file=out, end='')

if __name__ == "__main__":
    main()