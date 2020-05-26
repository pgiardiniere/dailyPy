# Given a sorted (ascending) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height.

# Okay, well since the array is sorted,
# We could simply do a binary-search over the array,

# Creating nodes in the following order:

#   root
#   root.left
#   root.right

#   root.left.left
#   root.left.right

# Seems a bit jank...


# Alternatively.
# We could create a 'dummy' tree of proper structure with
# placeholder data in 1st pass.

# Then in 2nd pass, fill in data by iterating through array
# using an in_order_traversal()

# O(2n) -> O(n) time ... ... 1 linear probe through array, 1 generation of tree
import numpy as np


# class SearchTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

#     def form_tree(self, node, size, i=0):
#         if i <= size:
#             print('foo')

#         if i+1 <= size:
#             left = self.Node(0)
#             node.left = left

#         if i <= size:
#             print('yay')  # self.form_tree()


def main():
    pass


if __name__ == '__main__':
    main()
