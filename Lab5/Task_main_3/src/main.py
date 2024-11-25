import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab5.utils import read_commands_s_n, write_lst_by_lines_file


class Node:
    def __init__(self, i, process_time, next=None, prev=None):
        self.idx = i
        self.proc_t = process_time
        self.next = next
        self.prev = prev
    
    def copy(self):
        return Node(self.idx, self.proc_t, self.next, self.prev)


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
            res.append((cur.arr_t, cur.proc_t))
            cur = cur.prev
        print(res)


class Buffer(Queue):
    def __init__(self):
        super().__init__()
        self.len = 0
        self.end_time = 0
        self.head_arrived_time = 0

    def put(self, node: Node, arrive_time):
        if self.head is None:
            self.head_arrived_time = arrive_time
        super().put(node)
        self.len += 1
        self.end_time += node.proc_t

    def pop(self):
        ret = super().pop()
        if ret is not None:
            self.len -= 1
        return ret
    
    def execute(self, fill_ans, time=None):
        cur_package = self.head
        if cur_package is None:
            return
        
        if time is None:
            time = self.end_time # till the end

        while self.head_arrived_time + cur_package.proc_t <= time: # is process executed before the new arrived
            fill_ans[cur_package.idx] = self.head_arrived_time

            self.head_arrived_time += cur_package.proc_t

            cur_package = cur_package.next
            if cur_package is None:
                break



def solution(s, packages):
    n = len(packages)
    buffer = Buffer()
    ans = [0] * n
    for i, command in enumerate(packages):
        arrive_time, process_time = map(int, command.split())
        process = Node(i, process_time)
        if buffer.head is None:
            buffer.put(process, arrive_time)
            continue
        if arrive_time >= buffer.end_time:
            buffer.execute(ans) # fill output with the whole buffer
            buffer.end_time = arrive_time
            buffer.put(process, arrive_time)
        else:
            buffer.execute(ans, arrive_time)
            if buffer.len != s:
                buffer.put(process, arrive_time)
            else:
                ans[i] = -1
    buffer.execute(ans)
    return ans

def main():
    s, lst = read_commands_s_n(os.path.join(PATH, 'txtf', 'input.txt'))
    res = solution(s, lst)
    write_lst_by_lines_file(os.path.join(PATH, 'txtf', 'output.txt'), res)


if __name__ == "__main__":
    main()