import os
import sys

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PATH, '..', '..'))

from Lab4.utils import read_n_lst_k, write_lst_file


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.stack:
            return
        return self.stack.pop()
    
    def peek(self):
        if not self.stack:
            return
        return self.stack[-1]
    
    def print(self, arg='', **kvargs):
        print(arg, self.stack, **kvargs)


class MaxStack(Stack):
    def __init__(self):
        super().__init__()
        self.max_stack = Stack()

    def push(self, element):
        super().push(element)
        last_max = self.max_stack.peek()
        if last_max is not None:
            self.max_stack.push(max(last_max, element))
        else:
            self.max_stack.push(element)

    def pop(self):
        self.max_stack.pop()
        return super().pop()

    def max(self):
        return self.max_stack.peek()
    
    def is_empty(self):
        return self.peek() is None
    
    def print(self):
        super().print(arg='stack:', end=' ')
        self.max_stack.print(arg='max:')


class QueueMax():
    def __init__(self):
        self.input_stack = MaxStack()
        self.output_stack = MaxStack()

    def peek(self):
        if self.output_stack.is_empty():
            while not self.input_stack.is_empty():
                self.output_stack.push(self.input_stack.pop())
        return self.output_stack.peek()


    def pop(self):
        if self.output_stack.is_empty():
            while not self.input_stack.is_empty():
                self.output_stack.push(self.input_stack.pop())
        return self.output_stack.pop()

    def put(self, value):
        self.input_stack.push(value)
    
    def peek_max(self):
        if self.input_stack.max() is None:
            return self.output_stack.max()
        if self.output_stack.max() is None:
            return self.input_stack.max()
        return max(self.input_stack.max(), self.output_stack.max())
    
    def print(self):
        print('inp/out')
        self.input_stack.print()
        self.output_stack.print()


def solution(n, lst, m):
    queue = QueueMax()
    for i in range(m):
        queue.put(lst[i])
        # queue.print()
    
    ans = [queue.peek_max()]
    for i in range(m, n):
        queue.pop()
        # queue.print()
        queue.put(lst[i])
        # queue.print()
        ans.append(queue.peek_max())

    return ans

def main():
    n, lst, m = read_n_lst_k(os.path.join(PATH, 'txtf', 'input.txt'))
    res = solution(n, lst, m)
    write_lst_file(os.path.join(PATH, 'txtf', 'output.txt'), res)


if __name__ == "__main__":
    main()