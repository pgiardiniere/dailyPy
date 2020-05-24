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


def kth_to_last(k, head):
    # Ensure we were passed a strictly positive int k
    if not isinstance(k, int) or k < 1:
        return None

    slow, fast = head, head

    # Iterate fast k positions ahead of slow. If len(list) < k, return None.
    for i in range(k):
        if fast.next is not None:
            fast = fast.next
        else:
            return None

    # Iterate both Node iters in sync. Return when fast hits end.
    while fast is not None:
        fast = fast.next
        slow = slow.next
    return slow


# Not working recursive sol'n
def rec_kth_to_last(k, node, size=0, j=0):
    if not isinstance(k, int) or k < 1:
        return None

    if node.next is None:
        if size - k == j:
            return node
        else:
            return (k, node, size+1, j)

    if node.next is not None:
        return rec_kth_to_last(k, node.next, size+1, j + 1)


def main():
    head = Node('one')
    head.append('two')
    head.append('three')
    head.append('four')
    head.append('five')

    head.print_all()
    print()

    print(kth_to_last(4, head).data)

    # print(rec_kth_to_last(4, head).data)


if __name__ == '__main__':
    main()


# Hints:
# 8
"""What if you knew the linked list size? What's the difference between finding
the Kth-to-last element and finding the Xth element?
"""
# 25
"""If you don't know the linked list's size, can you compute it?
How does this impact runtime?
"""
# 41
"""Try a recursive implementation. If you can findthe (K-1)th to last element,
can you find the Kth element?
"""
# 67
"""You might find it helpful to return multiple values.
Some languages don't directly support this, but there are workaround for any.
What are some of those workarounds?
"""
# 126
"""Can you do it iteratively? (yeah, already did)
... Use two pointers ... (abbreviated)
"""
