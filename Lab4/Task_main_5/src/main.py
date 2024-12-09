import os
import sys

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PATH, '..', '..'))

from Lab4.utils import read_commands, write_lst_by_lines_file


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.stack:
            return
        return self.stack.pop()
    
    def get_last(self):
        if not self.stack:
            return
        return self.stack[-1]


class MaxStack(Stack):
    def __init__(self):
        super().__init__()
        self.max_stack = Stack()

    def push(self, element):
        super().push(element)
        last_max = self.max_stack.get_last()
        if last_max is not None:
            self.max_stack.push(max(last_max, element))
        else:
            self.max_stack.push(element)

    def pop(self):
        self.max_stack.pop()
        return super().pop()

    def max(self):
        return self.max_stack.get_last()


def solution(commands):
    stack = MaxStack()
    res = []
    for command in commands:
        cmd = command.split()
        if cmd[0] == 'push':
            stack.push(int(cmd[1]))
        elif cmd[0] == 'pop':
            stack.pop()
        else:
            res.append(stack.max())
    return res

def main():
    lst = read_commands(os.path.join(PATH, 'txtf', 'input.txt'))
    res = solution(lst)
    write_lst_by_lines_file(os.path.join(PATH, 'txtf', 'output.txt'), res)


if __name__ == "__main__":
    main()