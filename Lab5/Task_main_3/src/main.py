import os
import sys

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PATH, '..', '..'))

from Lab5.utils import read_commands_s_n, write_lst_by_lines_file


class Node:
    def __init__(self, time, next=None, prev=None):
        self.time = time
        self.next = next
        self.prev = prev
    
    def copy(self):
        return Node(self.time, self.next, self.prev)


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def put(self, node: Node):
        if self.head is None:
            self.head = node
        elif self.tail is None:
            self.tail = node
            self.tail.next = self.head
            self.head.prev = self.tail
        else:
            prev_tail = self.tail
            self.tail = node
            self.tail.next = prev_tail
            prev_tail.prev = self.tail

    def pop(self):
        prev_head = self.head
        if prev_head is not None:
            new_head = self.head.prev
            if new_head is not None:
                new_head.next = None
            self.head = new_head

        return prev_head
    
    def peek(self):
        if self.head is not None:
            return self.head.copy()
        return None
    
    def peek_tail(self):
        if self.tail is not None:
            return self.tail.copy()
        return self.peek()
    
    def print(self):
        cur = self.head
        res = []
        while cur != None:
            res.append((cur.time))
            cur = cur.prev
        print(res)


class Buffer(Queue):
    def __init__(self):
        super().__init__()
        self.len = 0

    def put(self, node: Node):
        super().put(node)
        self.len += 1

    def pop(self):
        ret = super().pop()
        if ret is not None:
            self.len -= 1
        return ret


def solution(buffer_size, packages):
    buffer = Buffer()
    ans = []

    for package in packages:
        arrive_time, process_time = map(int, package.split())
        while buffer.peek() is not None and buffer.head.time <= arrive_time:
            buffer.pop()

        if buffer.len >= buffer_size:
            ans.append(-1)
        else:
            tail = buffer.peek_tail()
            if tail is None:
                start_time = arrive_time
            else:
                start_time = tail.time

            ans.append(start_time)

            buffer.put(Node(start_time + process_time))

    return ans

def main():
    s, lst = read_commands_s_n(os.path.join(PATH, 'txtf', 'input.txt'))
    res = solution(s, lst)
    write_lst_by_lines_file(os.path.join(PATH, 'txtf', 'output.txt'), res)


if __name__ == "__main__":
    main()