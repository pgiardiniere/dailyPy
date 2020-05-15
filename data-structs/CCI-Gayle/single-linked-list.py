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
        print(node.data)


if __name__ == '__main__':
    n = Node('first')
    n.add('second')
    n.add('third')
    n.print()
