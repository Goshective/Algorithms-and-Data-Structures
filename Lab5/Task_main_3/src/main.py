import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab5.utils import read_commands_s_n, write_lst_by_lines_file


class Node:
    def __init__(self, arrive_time, process_time, next=None, prev=None):
        self.arr_t = arrive_time
        self.proc_t = process_time
        self.next = next
        self.prev = prev
    
    def copy(self):
        return Node(self.arr_t, self.proc_t, self.next, self.prev)


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
        return self.head.copy()
    
    def print(self):
        cur = self.head
        res = []
        while cur != None:
            res.append((cur.arr_t, cur.proc_t))
            cur = cur.prev
        print(res)

class Buffer(Queue):
    def __init__(self):
        super().__init__()
        self.len = 0
        self.end_time = 0

    def put(self, node: Node):
        super().put(node)
        self.len += 1
        self.end_time += node.proc_t

    def pop(self):
        ret = super().pop()
        if ret is not None:
            self.len -= 1
        return ret
    
    def execute(self, fill_ans, time=None):
        if time is None:
            time = self.end_time


def solution(s, packages):
    n = len(packages)
    buffer = Queue()
    ans = [0] * n
    for i, command in enumerate(packages):
        arrive_time, process_time = map(int, command.split())
        process = Node(arrive_time, process_time)
        if arrive_time >= buffer.end_time:
            buffer.execute(ans) # fill output
            buffer.end_time = arrive_time
            buffer.put(process)
        elif buffer.len < s:
            buffer.execute(ans, arrive_time)
            buffer.put(process)
        else:
            ans[i] = -1
    return ans

def main():
    s, lst = read_commands_s_n(os.path.join(PATH, 'txtf', 'input.txt'))
    res = solution(s, lst)
    write_lst_by_lines_file(os.path.join(PATH, 'txtf', 'output.txt'), res)


if __name__ == "__main__":
    main()