# Using a SINGLE-linked list
# a->b->c->d->e->f
# a->b->d->e->f

# Hint #72:
"""Picture the list 1 -> 5 -> 9 -> 12. Removing 9 would make it look
like 1 -> 5 -> 12. Only have access to 9 node.
Can you make it look like the correct answer?
"""
# Oh, in that case, we update Node's data and set next to next.next
# but, we'd have to do that for all nodes assuming 9 is not next-to-last node.


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

    def add(self, d):
        new_node = Node(d)
        n = self
        while n.next is not None:
            n = n.next
        n.next = new_node
        return new_node

    def print_list(self):
        n = self
        while n.next is not None:
            print(n.data)
            n = n.next
        print(n.data, end='\n\n')


def delete_middle(n):
    while n.next is not None:
        n.data = n.next.data
        trail = n
        n = n.next
    trail.next = None

# O(n) time complexity, single linear probe through list.

# Ah hell, this is bad.
# Solution is O(1) time, and much more straightforward...


# Solution:
def delete_mid(n):
    if n is None or n.next is None:
        return False
    next = n.next
    n.data = next.data
    n.next = next.next
    return True


if __name__ == '__main__':
    # test:
    head = Node('a')
    b = head.add('b')
    c = head.add('c')
    head.add('d')

    head.print_list()
    # delete_middle(c)
    delete_mid(c)
    head.print_list()
