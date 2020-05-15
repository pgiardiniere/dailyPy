class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def add(self, data):
        tail = Node(data)
        node = self
        while node.next is not None:
            node = node.next
        node.next = tail

    def print(self):
        node = self
        while node.next is not None:
            print(node.data)
            node = node.next
        print(node.data, end='\n\n')

    def delete(self, dat):
        node = self

        if (node.data == dat):
            return node.next

        while node.next is not None:
            if node.next.data == dat:
                node.next = node.next.next
                return self
            node = node.next

        return self


if __name__ == '__main__':
    n = Node('first')
    n.add('second')
    n.add('third')
    n.print()

    n = n.delete('first')
    n.print()

    n = n.delete('second')
    n.print()

    # n = n.delete('third')
    # n.print()
