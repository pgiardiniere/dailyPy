# Simple tree structure: Basic Binary Tree


class Node:
    def __init__(self, data_item_1, data_item_2):
        self.d1 = data_item_1
        self.d2 = data_item_2
        self.left = None
        self.right = None

    def visit(self, node):
        print(node.d1, end=' ')
        print(node.d2, end='\n')

    def in_order_traverse(self, node):
        if node is not None:
            self.in_order_traverse(node.left)
            self.visit(node)
            self.in_order_traverse(node.right)

    def pre_order_traverse(self, node):
        if node is not None:
            self.visit(node)
            self.in_order_traverse(node.left)
            self.in_order_traverse(node.right)

    def post_order_traverse(self, node):
        if node is not None:
            self.in_order_traverse(node.left)
            self.in_order_traverse(node.right)
            self.visit(node)


# Next: Binary Heap (i.e. Binary Min-Heap).
# A binary min-heap is a binary tree with the property that is both...
#   Complete, and
#   every node is smaller than its children. Root is min of whole tree.

# Insertion and removal both involve 'bubbling' of elements, are O(log(n))
