# This is a Python port of my Java sudoku solver written for 2168: Data Structs

# Difference: Use a deque for an iterative solution instead of tail recursion,
# as using tail-recursion exceeds default max recursion depth for stack frames.

# Track state in the deque using an ordered 3-tuples of (row, col, value)
from collections import deque


class Sudoku:
    def __init__(self):
        self.board = [
            [9, 6, 0, 0, 1, 0, 2, 0, 8],
            [0, 8, 0, 5, 0, 0, 1, 9, 4],
            [0, 0, 5, 2, 0, 0, 0, 0, 6],
            [0, 0, 0, 0, 2, 9, 3, 4, 0],
            [0, 0, 0, 8, 0, 6, 0, 0, 0],
            [0, 9, 2, 4, 3, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 7, 8, 0],
            [6, 7, 9, 0, 0, 2, 0, 1, 0],
            [5, 0, 8, 0, 4, 0, 0, 7, 3]
        ]

    def board_print(self):
        for i in range(9):
            for j in range(9):
                print(self.board[i][j], end=' ')
                if (j == 8):
                    print()
        print()

    def pretty_print(self, output):
        for i in range(9):
            if i > 0 and i % 3 == 0:
                print('---------------------', file=output)
            for j in range(9):
                if (j > 0 and j % 3 == 0):
                    print('|', end=' ', file=output)
                print(self.board[i][j], end=' ', file=output)
                if (j == 8):
                    print(file=output)
        print(file=output)

    def isFull(self):
        for i in range(10):
            for j in range(10):
                if (self.board[i][j] == 0):
                    return False
        return True


def find_next(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return (-1, -1)


def valid_move(board, row, col, val):
    for j in range(9):
        if board[row][j] == val:
            return False

    for i in range(9):
        if board[i][col] == val:
            return False

    tile = (row - row % 3, col - col % 3)
    for i in range(tile[0], tile[0] + 3):
        for j in range(tile[1], tile[1] + 3):
            if board[i][j] == val:
                return False

    return True


def solve(sudoku, output):
    d = deque()
    row, col = find_next(sudoku.board)
    d.append((row, col, 0))

    # if (row == -1):
    #     return True

    while not sudoku.isFull() and d:
        t = d.pop()

        for val in range(t[2]+1, 10):
            if valid_move(sudoku.board, t[0], t[1], t[2]+1):
                sudoku.board[t[0]][t[1]] = val
                d.append((t[0], t[1], val))

        # If that row/col was not updated, we must backtrack. Else, advance.
        if sudoku.board[t[0]][t[1]] == t[2]:
            sudoku.board[t[0]][t[1]] = 0

        else:
            row, col = find_next(sudoku.board)
            d.append((row, col, 0))


# def solve(sudoku, output):
#     row, col = find_next(sudoku.board)
#     if (row == -1):
#         return True

#     for val in range(1, 10):
#         if valid_move(sudoku.board, row, col, val):
#             sudoku.board[row][col] = val

#     if (solve(sudoku, output)):
#         return True
#     else:
#         sudoku.board[row][col] = 0
#     return False


if __name__ == '__main__':
    sudoku = Sudoku()
    output = open('output.txt', 'w')

    sudoku.pretty_print(output)
    solve(sudoku, output)
    sudoku.pretty_print(output)

    output.close()
