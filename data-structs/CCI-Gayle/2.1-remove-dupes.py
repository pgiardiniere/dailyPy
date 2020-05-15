"""2.1 - Remove Duplicates:
Write code to remove duplicates from an unsorted linked list.
Then, solve this problem without a temporary buffer.
"""

# Okay, so our first solution will have temp list
# Second solution will involve... an in-place sort? not sure.


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

    def print_list(self):
        n = self
        while n.next is not None:
            print(n.data, end=' ')
            n = n.next
        print(n.data, end='\n\n')

    def add(self, d):
        new = Node(d)
        n = self

        while n.next is not None:
            n = n.next

        n.next = new


# O(n) time complexity      (linearly probe 1 time)
# O(n) spatial complexity   (buffer of size n els)
def buffered_dupe_remove(node):
    if node is None or node.next is None:
        return node

    hashes = []
    prev = node

    while node.next is not None:
        h = hash(node.data)
        if h in hashes:
            prev.next = node.next
        else:
            hashes.append(h)

        prev = node
        node = node.next


def dupe_remove(node):
    while node is not None:
        runner = node
        while runner.next is not None:
            if runner.next.data == node.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        node = node.next


# Hint #9:
"""Have you tried a hash table?
"""

# Hint #70:
"""Without extra space, you'll need O(N^2) time. Try using two pointers,
with the second pointer being ahead of hte first.
"""

# Okay, so I got the intent of both hints. Buffered sol'n already done.

# Non-buffered sol'n is ugly as hell though...
# Oh, I'm unnecessarily counting my current node 'n' forwards each run.

if __name__ == '__main__':
    head = Node(1)
    head.add(2)
    head.add(2)
    head.add(3)
    head.add(2)
    head.add(4)

    head.print_list()
    buffered_dupe_remove(head)
    head.print_list()

    head = Node(1)
    head.add(2)
    head.add(2)
    head.add(3)
    head.add(2)
    head.add(4)

    head.print_list()
    dupe_remove(head)
    head.print_list()
