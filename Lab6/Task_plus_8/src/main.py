import os
import sys
from array import array


EMPTY = 10**15+1
PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..', '..'))

from Lab6.utils import read_file, write_lst_file


class HashSet:
    def __init__(self, max_size):
        self.size = 0
        self.table = array('q', [EMPTY] * max_size)
        self.aux_list = []
        self.max_size = max_size

    def _hash(self, k):
        return k % self.max_size

    # def add(self, k):
    #     index = self._hash(k)

    #     if self.table[index] is None:
    #         self.table[index] = [k]
    #         self.size += 1
    #         return
        
    #     cur_node = self.table[index]

    #     for key in cur_node:
    #         if key == k:
    #             return

    #     cur_node.append(k)
    #     self.size += 1

    #     return
    
    def add(self, k):
        index = self._hash(k)

        if self.table[index] == EMPTY:
            self.table[index] = k
            self.size += 1
            return
        
        cur_value = self.table[index]
        if cur_value == k: return

        if cur_value >= 0:
            idx = len(self.aux_list)
            lst = [cur_value, k]
            self.aux_list.append(lst)
            self.table[index] = cur_value = -idx
        else:
            lst = self.aux_list[-cur_value]
            for key in lst:
                if key == k: return
            lst.append(k)
        self.size += 1
    
    # def __contains__(self, k):
    #     index = self._hash(k)
    #     cur_node = self.table[index]
    #     return k in cur_node if cur_node is not None else False
    
    def __contains__(self, k):
        index = self._hash(k)
        cur_node = self.table[index]
        if cur_node == EMPTY:
            return False
        elif cur_node >= 0:
            return cur_node == k

        return k in self.aux_list[-cur_node]

    def __len__(self): 
        return self.size


def solution(lst):
    n,x,a,b, ac,bc,ad,bd = lst
    size = n * 2 if n < 10**6 else 2017963
    hash_set = HashSet(size) # prime for distribution
    t = 10 ** 15
    for _ in range(n):
        if x in hash_set:
            a = (a + ac) % 1000
            b = (b + bc) % t
        else:
            a = (a + ad) % 1000
            b = (b + bd) % t
            hash_set.add(x)
        x = (x * a + b) % t
    return x, a, b

def main():
    func = lambda x: list(map(int, x.split()))
    inp = read_file(os.path.join(PATH, 'txtf', 'input.txt'), func, func)
    res = solution(inp[0] + inp[1])
    write_lst_file(os.path.join(PATH, 'txtf', 'output.txt'), res)


if __name__ == "__main__":
    main()