# You have two numbers represented by a linked list,
# where each node contains a single digit.
# Digits are stored in reverse order, i.e. 1's digit is at head of list.
# Write a function which adds the two nums and returns sum as a linked list.

# Input:
# (7 -> 1 -> 6) + (5 + 9 + 2)  is  617 + 295

# Output:
# (2 -> 1 -> 9)   i.e. 912


# Follow up: suppose digits are stored in forwards order.
# Repeat the above problem.

# import numpy as np  # noqa


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, data):
        node = self

        while node.next is not None:
            node = node.next

        node.next = Node(data)

    def list_print(self):
        node = self

        while node is not None:
            print(node.data, end='-> ')
            node = node.next
        print('\n')


# get num_digits without a slow string conversion
import math  # noqa
def num_digits(num):  # noqa
    if num > 0:
        return int(math.log10(num) + 1)
    if num == 0:
        return 1
    if num < 0:
        return int(math.log10(-num) + 1)


# quick-and-dirty num-digits sol'n: convert to/from string.
def create_list(ans):
    s = str(ans)
    i = len(s) - 1

    if i > -1:
        node = Node(s[i])
        i -= 1

    while i > -1:
        node.append(s[i])
        i -= 1

    return node


def sum_lists(L1, L2):
    x1, place = 0, 1
    while L1 is not None:
        x1 += L1.data * place
        place *= 10
        L1 = L1.next

    x2, place = 0, 1
    while L2 is not None:
        x2 += L2.data * place
        place *= 10
        L2 = L2.next

    ans = x1 + x2
    return create_list(ans)


def main():
    # Create text example:
    L1 = Node(7)
    L1.append(1)
    L1.append(6)

    L2 = Node(5)
    L2.append(9)
    L2.append(2)

    L1.list_print()
    L2.list_print()

    L3 = sum_lists(L1, L2)
    L3.list_print()

    # test num_digits()


if __name__ == '__main__':
    main()
