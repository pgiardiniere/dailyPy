
class BSTNode:
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


def main():
    r = BSTNode(5)
    insert(r, BSTNode(3))
    insert(r, BSTNode(2))
    insert(r, BSTNode(4))
    insert(r, BSTNode(7))
    insert(r, BSTNode(6))
    insert(r, BSTNode(8))

    in_order_walk(r)


if __name__ == '__main__':
    main()
