# This is a Python port of my Java sudoku solver written for 2168: Data Structs
# Against my better judgment, we'll do this with plain old Lists first time around.

class Sudoku:
    def __init__(self):
        self.board = [
            [9, 6, 0, 0, 1, 0, 2, 0, 8],
            [0, 8, 0, 5, 0, 0, 1, 9, 4],
            [0, 0, 0, 0, 2, 9, 3, 4, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

    def board_print(self):
        for i in range(9):
            for j in range(9):
                print(self.board[i][j], end=' ')
                if (j == 8): print()
        print()

    def pretty_print(self):
        for i in range(9):
            if (i > 0 and i % 3 == 0):
                print('---------------------')
            for j in range(9):
                if (j > 0 and j % 3 == 0):
                    print('|', end=' ')
                print(self.board[i][j], end=' ')
                if (j == 8): 
                    print()
        print()
    

def main():
    sudoku = Sudoku()

    sudoku.board_print()
    sudoku.pretty_print()

    sudoku.board[0][0] = 'F'
    sudoku.pretty_print()

main()
