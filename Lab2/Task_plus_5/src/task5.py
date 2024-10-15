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

def main():
    path = os.path.dirname(os.path.abspath(__file__)) + '/'
    with open(path+'input.txt', 'r') as inp, open(path+'output.txt', 'w') as out:
        n = int(inp.readline())
        lst = [int(x) for x in inp.readline().split()]
        res = solution(n, lst)
        print(res, file=out, end='')
    return

if __name__ == "__main__":
    main()