# Return Kth to Last:
# Implement an algorithm to find the kth to last element of a singly-linked list.

# Hints: 8, 25, 41, 67, 126
import numpy as np  # noqa


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, data):
        new_node = Node(data)
        node = self

        while node.next is not None:
            node = node.next
        node.next = new_node

    def print_all(self):
        node = self

        while node is not None:
            print(node.data)
            node = node.next


if __name__ == '__main__':
    head = Node('one')
    head.append('two')
    head.append('three')

    head.print_all()
