from board import *


def solve(i: int, j: int) -> bool:
    if i == SIZE:
        return True  # Reached end of matrix

    if board.mat[i][j].is_const:  # This tile is constant
        return solve(i + ((j + 1) // SIZE),
                     (j + 1) % SIZE)  # Advancing to the next tile

    for val in range(1, SIZE + 1):
        if board.set_tile(i, j, val):
            if solve(i + ((j + 1) // SIZE), (j + 1) % SIZE):
                return True
    # None of the values fit, backtracking
    board.reset_tile(i, j)
    return False


def init_tiles(matrix):
    while True:
        inpt = input("Enter tile in format <row,col,val>, \n"
                     "or type 'solve' to finish: ")

        if inpt.lower() == "solve":
            return
        try:
            row, col, val = [int(k) for k in inpt.split(",")]
        except ValueError:
            print("Invalid input. Try again.\n")
            continue

        try:
            matrix.init_tile(row, col, val)
        except AttributeError as err:
            print(err, "\nTry a different setting\n")
        except ValueError as err:
            print(err, "\nTry setting a different one\n")
            matrix.reset_tile(row, col)


def board_printer(board):
    """Prints the sudoku board"""
    print()
    for row in range(SIZE):
        s = ''
        for col in range(SIZE):
            s += str(board.mat[row][col]) + '  '
            if not (col + 1) % 3:
                s += '| '
        s = s[:-2]  # Removes trailing space
        print(s)

        if (not (row + 1) % 3 ) and row+1 !=SIZE :
            print('-' * len(s))
    print("\n")


if __name__ == '__main__':
    board = Board()
    init_tiles(board)

    print("INITIAL BOARD: ")

    board_printer(board)

    if not solve(0, 0):
        print("Board is not solvable!")
        exit(1)

    print("SOLVED BOARD: ")
    board_printer(board)
