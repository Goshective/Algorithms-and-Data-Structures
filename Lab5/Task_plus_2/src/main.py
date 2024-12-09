import os
import sys

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PATH, '..', '..'))

from Lab5.utils import read_n_lst, write_file

class Node:
    def __init__(self, idx):
        # self.parent = None
        self.children = []
        self.idx = idx

    def add_children_connection(self, node: 'Node'):
        self.children.append(node.idx)
        # node.parent = self.idx

    def get_children(self):
        return self.children.copy()

    def print(self):
        print(self.idx, "-", self.children)


class Tree:
    def __init__(self, tree_list):
        self.index_tree = tree_list
        self.fill_tree()
        self.root = self.node_tree[-1]

    def fill_tree(self):
        self.node_tree = [None] * (len(self.index_tree) + 1) # for root node (last)
        fast_search_parent = {}

        for node_idx, parent_idx in enumerate(self.index_tree):
            fast_search_parent[parent_idx] = fast_search_parent.get(parent_idx, []) + [node_idx]
            

        stack = [-1]
        while stack:
            parent_idx = stack.pop()

            if self.node_tree[parent_idx] is None:
                self.node_tree[parent_idx] = Node(parent_idx)

            if parent_idx in fast_search_parent:
                for child_idx in fast_search_parent[parent_idx]:
                    stack.append(child_idx)
                    child_node = Node(child_idx)
                    self.node_tree[parent_idx].add_children_connection(child_node)
                    self.node_tree[child_idx] = child_node
    
    def print(self):
        self.root.print()
        stack = self.root.get_children()
        while stack:
            node = self.node_tree[stack.pop()]
            node.print()
            for child in node.get_children():
                stack.append(child)

    def get_node_by_index(self, idx) -> Node:
        if idx == -1:
            return self.root
        if 0 <= idx < len(self.node_tree):
            return self.node_tree[idx]
        return None

    def get_height(self):
        stack = [(self.root.idx, 0)]
        max_height = 0
        while stack:
            node_idx, height = stack.pop()
            node = self.get_node_by_index(node_idx)

            for child_node in node.get_children():
                stack.append((child_node, height + 1))
            
            max_height = max(max_height, height)

        return max_height


def solution(lst):
    tree = Tree(lst)
    # tree.print()
    return tree.get_height()

def main():
    _, lst = read_n_lst(os.path.join(PATH, 'txtf', 'input.txt'))
    res = solution(lst)
    write_file(os.path.join(PATH, 'txtf', 'output.txt'), res)


if __name__ == "__main__":
    main()