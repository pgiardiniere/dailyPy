# https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/ 
# More-or-less rip from site. My impl. below.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, node):
    if root is None:
        root = node

    elif root.data < node.data:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)

    else:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)


def in_order_walk(root):
    if root is not None:
        in_order_walk(root.left)
        print(root.data)
        in_order_walk(root.right)


# My implementation
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_ordered(self, data):
        root = self

        if root.data < data:
            if root.right is None:
                root.right = self.__init__(data)
            else:
                self.insert_ordered(root.right, data)

        else:
            if root.left is None:
                root.left = self.__init__(data)
            else:
                self.insert_ordered(root.left, data)

    def in_order_walk(self, root):
        if root is not None:
            self.in_order_walk(root.left)
            print(root.data)
            self.in_order_walk(root.right)


def main():
    r = Node(5)
    insert(r, Node(3))
    insert(r, Node(2))
    insert(r, Node(4))
    insert(r, Node(7))
    insert(r, Node(6))
    insert(r, Node(8))

    in_order_walk(r)

    print('\n')

    r2 = BSTNode(5)
    r2.insert_ordered(3)
    r2.insert_ordered(2)
    r2.insert_ordered(4)
    r2.insert_ordered(7)
    r2.insert_ordered(6)
    r2.insert_ordered(8)

    r2.in_order_walk(r2)


if __name__ == '__main__':
    main()
