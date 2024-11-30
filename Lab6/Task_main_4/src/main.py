import os
import sys


PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab6.utils import read_commands, write_lst_by_lines_file

class Node: 
    def __init__(self, key, value): 
        self.key = key 
        self.value = value 
        self.next = None

        self.next_arr = None
        self.prev_arr = None


class HashTable:
    def __init__(self, max_size):
        self.size = 0
        self.table = [None] * max_size
        self.max_size = max_size

    def _hash(self, k):
        return hash(k) % self.max_size

    def insert(self, k, v) -> Node:
        index = self._hash(k)

        if self.table[index] is None:
            self.table[index] = Node(k, v)
            self.size += 1
            return self.table[index]
        
        cur_node = self.table[index]

        while cur_node is not None:
            if cur_node.key == k:
                cur_node.value = v
                return cur_node
            cur_node = cur_node.next

        new_node = Node(k, v)
        new_node.next = self.table[index]
        self.table[index] = new_node
        self.size += 1

        return new_node
    
    def search(self, k, mode=None) -> Node:
        index = self._hash(k)
        cur_node = self.table[index]
        while cur_node is not None:
            if cur_node.key == k:
                return (cur_node.value if mode is None else cur_node)
            cur_node = cur_node.next
        return None # raise KeyError(key)
    
    def remove(self, k) -> Node:
        index = self._hash(k)
        prev = None
        cur_node = self.table[index]
        
        while cur_node is not None:
            if cur_node.key == k:
                if prev is None:
                    self.table[index] = cur_node.next
                else:
                    prev.next = cur_node.next
                self.size -= 1
                return cur_node ############
            prev = cur_node
            cur_node = cur_node.next

        return None
        # raise KeyError(key)

    def __len__(self): 
        return self.size
    
    def __contains__(self, k):
        return self.search(k) is None
    

class AssociationArray(HashTable):
    def __init__(self, max_size):
        super().__init__(max_size)
        self.head = None

    def insert(self, k, v):
        node = super().insert(k, v)
        if self.head is not None:
            connect(self.head, node)
        self.head = node

    def remove(self, k):
        node = super().remove(k)
        if node is not None:
            reconnect(node)

    def prev(self, k):
        node = super().search(k, mode="Node")
        if node is not None and node.prev_arr is not None:
            return node.prev_arr.value
        return None
    
    def next(self, k):
        node = super().search(k, mode="Node")
        if node is not None and node.next_arr is not None:
            return node.next_arr.value
        return None

def connect(node1, node2):
    if node1 is not None:
        node1.next_arr = node2
    if node2 is not None:
        node2.prev_arr = node1

def reconnect(node):
    connect(node.prev_arr, node.next_arr)


def solution(commands):
    dct = AssociationArray(len(commands))
    ans = []
    for command in commands:
        cmd = command.split()
        if cmd[0] == 'put':
            dct.insert(cmd[1], cmd[2])
        elif cmd[0] == 'delete':
            dct.remove(cmd[1])
        elif cmd[0] in ('get', 'prev', 'next'):
            if cmd[0] in 'get':
                ret = dct.search(cmd[1])
            elif cmd[0] == 'prev':
                ret = dct.prev(cmd[1])
            else:
                ret = dct.next(cmd[1])
            ans.append("<none>" if (ret is None) else ret)
    return ans

def main():
    lst = read_commands(os.path.join(PATH, 'txtf', 'input.txt'))
    res = solution(lst)
    write_lst_by_lines_file(os.path.join(PATH, 'txtf', 'output.txt'), res)


if __name__ == "__main__":
    main()