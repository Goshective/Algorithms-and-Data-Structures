import os
import sys

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PATH, '..', '..'))

from Lab4.utils import read_file, write_file


def solution(line):
    is_open = {'(': True, '[': True, '{': True,
               ')': False, ']': False, '}': False}
    clone = {')': '(', ']': '[', '}': '{'}
    stack = []
    for i, symb in enumerate(line):
        symb = line[i]
        if symb not in is_open:
            continue
        if is_open[symb]:
            stack.append(symb)
        elif stack and stack[-1] == clone[symb]:
            stack.pop()
        else:
            return i + 1
    if not stack:
        return 'Success'
    return len(line)



def main():
    line = read_file(os.path.join(PATH, 'txtf', 'input.txt'), str)[0]
    res = solution(line)
    write_file(os.path.join(PATH, 'txtf', 'output.txt'), res)


if __name__ == "__main__":
    main()