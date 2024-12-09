import os
import sys

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PATH, '..', '..'))
sys.set_int_max_str_digits(5000)

from Lab6.utils import read_commands, write_lst_by_lines_file


def fill_fib(x, last_n):
    global fibs
    global fibs_by_num
    i = last_n
    while True:
        new_fib = fibs_by_num[i-1] + fibs_by_num[i]
        fibs.add(new_fib)
        fibs_by_num.append(new_fib)
        i += 1
        if new_fib > x:
            return False, i
        elif new_fib == x:
            break
    return True, i
    


def solution(lst):
    global fibs
    global fibs_by_num
    fibs = set([1])
    fibs_by_num = [1, 1]
    res = []
    last_n = 1
    for i in lst:
        x = int(i)
        if x not in fibs:
            if x > fibs_by_num[last_n]:
                verdict, last_n = fill_fib(x, last_n)
                res.append("Yes" if verdict else "No")
            else:
                res.append("No")    
        else:
            res.append("Yes")

    return res


def main():
    lst = read_commands(os.path.join(PATH, 'txtf', 'input.txt'))
    res = solution(lst)
    write_lst_by_lines_file(os.path.join(PATH, 'txtf', 'output.txt'), res)


if __name__ == "__main__":
    main()