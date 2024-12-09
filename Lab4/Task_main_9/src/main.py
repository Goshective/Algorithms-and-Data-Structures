import os
import sys

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PATH, '..', '..'))

from Lab4.utils import read_commands, write_lst_by_lines_file


class Node:
    def __init__(self, value, next=None, prev=None):
        self.val = value
        self.next = next
        self.prev = prev

    def put_between(self, node1: 'Node', node2: 'Node'):
        if node1 is None and node2 is None:
            return
        
        if node2 is not None:
            self.next = node2
            node2.prev = self

        if node1 is not None:
            self.prev = node1
            node1.next = self




class QueueMid:
    def __init__(self):
        self.head = None
        self.tail = None
        self.to_mid = None
        self.len = 0

    def put(self, node: Node):
        if self.head is None:
            self.head = node
            self.to_mid = self.head
        elif self.tail is None:
            self.tail = node
            self.tail.next = self.head
            self.head.prev = self.tail
            self.to_mid = self.head
        else:
            prev_tail = self.tail
            self.tail = node
            self.tail.next = prev_tail
            prev_tail.prev = self.tail

            if self.len % 2 == 0:
                self.to_mid = self.to_mid.prev

        self.len += 1

    def put_to_mid(self, node: Node):
        if self.head is None or self.tail is None:
            self.put(node)
            return
        else:
            prev_from_mid = self.to_mid.prev
            next_from_mid = self.to_mid
            node.put_between(prev_from_mid, next_from_mid)

        if self.len % 2 == 0:
            self.to_mid = self.to_mid.prev

        self.len += 1

    def get(self):
        prev_head = self.head
        if prev_head is not None:
            new_head = self.head.prev
            if new_head is not None:
                new_head.next = None
            self.head = new_head

            self.len -= 1

        return prev_head
    
    def print(self):
        cur = self.head
        res = []
        while cur != None:
            res.append(cur.val)
            cur = cur.prev
        print(res)


def solution(lst):
    queue = QueueMid()
    ans = []
    for command in lst:
        cmd = command.split()
        if cmd[0] == '+':
            queue.put(Node(int(cmd[1])))
        elif cmd[0] == '*':
            queue.put_to_mid(Node(int(cmd[1])))
        else:
            ret = queue.get()
            ans.append(ret.val)
        # queue.print()
    return ans

def main():
    lst = read_commands(os.path.join(PATH, 'txtf', 'input.txt'))
    res = solution(lst)
    write_lst_by_lines_file(os.path.join(PATH, 'txtf', 'output.txt'), res)


if __name__ == "__main__":
    main()