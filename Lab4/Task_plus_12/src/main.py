import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
LEFT = 0
RIGHT = 1
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab4.utils import read_commands_n_m, write_mat_by_lines_file


class Node:
    def __init__(self, value, next=None, prev=None):
        self.val = value
        self.next = next
        self.prev = prev

    def put_between(self, node1: 'Node', node2: 'Node'):
        if node2 is not None:
            self.next = node2
            node2.prev = self

        if node1 is not None:
            self.prev = node1
            node1.next = self

    def pop(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.next = None
        self.prev = None

    def name(self):
        res = [(0 if self.prev is None else self.prev.val), 
               (0 if self.next is None else self.next.val)]
        return res


class LinkedListDictionary:
    def __init__(self, n):
        self.dct = {i: Node(i) for i in range(1, n + 1)}

    def put(self, node_put_idx, node2_idx, turn):
        if node_put_idx is not None:
            node_put = self.dct[node_put_idx]
        if node2_idx is not None:
            node2 = self.dct[node2_idx]
        
            if turn == LEFT:
                node1 = node2.prev
                node_put.put_between(node1, node2)
            else:
                node1 = node2.next
                node_put.put_between(node2, node1)
    
    def pop(self, node_idx):
        node = self.dct[node_idx]
        node.pop()

    def name(self, node_idx):
        node = self.dct[node_idx]
        return node.name()


def solution(n, commands):
    linked_list = LinkedListDictionary(n)
    linked_list.put(1, None, LEFT)
    ans = []
    for command in commands:
        cmd = command.split()
        if cmd[0] == 'left':
            node1_idx = int(cmd[1])
            node2_idx = int(cmd[2])
            linked_list.put(node1_idx, node2_idx, LEFT)
        elif cmd[0] == 'right':
            node1_idx = int(cmd[1])
            node2_idx = int(cmd[2])
            linked_list.put(node1_idx, node2_idx, RIGHT)
        elif cmd[0] == 'leave':
            node_idx = int(cmd[1])
            linked_list.pop(node_idx)
        else:
            node_idx = int(cmd[1])
            ans.append(linked_list.name(node_idx))
    return ans

def main():
    n, commands = read_commands_n_m(os.path.join(PATH, 'txtf', 'input.txt'))
    res = solution(n, commands)
    write_mat_by_lines_file(os.path.join(PATH, 'txtf', 'output.txt'), res)


if __name__ == "__main__":
    main()