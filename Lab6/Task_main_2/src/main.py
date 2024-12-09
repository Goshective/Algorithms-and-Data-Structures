import os
import sys

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PATH, '..', '..'))

from Lab6.utils import read_commands, write_lst_by_lines_file

class Node: 
    def __init__(self, key, value): 
        self.key = key 
        self.value = value 
        self.next = None

class HashTable:
    def __init__(self, max_size):
        self.size = 0
        self.table = [None] * max_size
        self.max_size = max_size

    def _hash(self, k):
        return hash(k) % self.max_size

    def insert(self, k, v):
        index = self._hash(k)

        if self.table[index] is None:
            self.table[index] = Node(k, v)
            self.size += 1
        else:
            cur_node = self.table[index]
            while cur_node is not None:
                if cur_node.key == k:
                    cur_node.value = v
                    return
                cur_node = cur_node.next

            new_node = Node(k, v)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1
    
    def search(self, k):
        index = self._hash(k)
        cur_node = self.table[index]
        while cur_node is not None:
            if cur_node.key == k:
                return cur_node.value
            cur_node = cur_node.next
        return None # raise KeyError(key)
    
    def remove(self, k):
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
                return
            prev = cur_node
            cur_node = cur_node.next

        # raise KeyError(key)

    def __len__(self): 
        return self.size


def solution(commands):
    dct = HashTable(len(commands))
    ans = []
    for command in commands:
        cmd = command.split()
        if cmd[0] == 'add':
            dct.insert(int(cmd[1]), cmd[2])
        elif cmd[0] == 'del':
            dct.remove(int(cmd[1]))
        else:
            ret = dct.search(int(cmd[1]))
            ans.append("not found" if (ret is None) else ret)
    return ans

def main():
    lst = read_commands(os.path.join(PATH, 'txtf', 'input.txt'))
    res = solution(lst)
    write_lst_by_lines_file(os.path.join(PATH, 'txtf', 'output.txt'), res)


if __name__ == "__main__":
    main()