"""
Q: Su Doku (Japanese meaning number place) is the name given to a popular puzzle
concept. Its origin is unclear, but credit must be attributed to Leonhard Euler
who invented a similar, and much more difficult, puzzle idea called Latin
Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or
zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains
each of the digits 1 to 9. Below is an example of a typical starting puzzle grid
and its solution grid.

  0 0 3 0 2 0 6 0 0    4 8 3 9 2 1 6 5 7
  9 0 0 3 0 5 0 0 1    9 6 7 3 4 5 8 2 1
  0 0 1 8 0 6 4 0 0    2 5 1 8 7 6 4 9 3
  0 0 8 1 0 2 9 0 0    5 4 8 1 3 2 9 7 6
  7 0 0 0 0 0 0 0 8    7 2 9 5 6 4 1 3 8
  0 0 6 7 0 8 2 0 0    1 3 6 7 9 8 2 4 5
  0 0 2 6 0 9 5 0 0    3 7 2 6 8 9 5 1 4
  8 0 0 2 0 3 0 0 9    8 1 4 2 5 3 7 6 9
  0 0 5 0 1 0 3 0 0    6 9 5 4 1 7 3 8 2

A well constructed Su Doku puzzle has a unique solution and can be solved by
logic, although it may be necessary to employ "guess and test" methods in order
to eliminate options (there is much contested opinion over this). The complexity
of the search determines the difficulty of the puzzle; the example above is
considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'),
contains fifty different Su Doku puzzles ranging in difficulty, but all with
unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the
top left corner of each solution grid; for example, 483 is the 3-digit number
found in the top left corner of the solution grid above.

A: 24702
"""


class Sudoku:
    def __init__(self, name, board):
        self.name = name
        self.original_board = [list(row) for row in board]
        self.solved_board = self.solve(board)

    def solve(self, board):
        if self.board_is_filled(board):
            if self.board_is_valid(board):
                return board

            return False

        i, j = self.first_empty_cell(board)
        for num in self.possible_nums(i, j, board):
            # fill the first empty cell with a candidate number
            board[i][j] = num
            done = self.solve(board)
            if done:
                return board

            # undo the setting of cell (i, j)
            board[i][j] = 0

        return False

    def board_is_filled(self, board):
        for row in board:
            for n in row:
                if n == 0:
                    return False

        return True

    def board_is_valid(self, board):
        # rows have digits 1--9
        for row in board:
            if sorted(list(set(row))) != list(range(1, len(board) + 1)):
                return False

        # columns have digits 1--9
        for col in zip(*board):
            if sorted(list(set(col))) != list(range(1, len(board[0]) + 1)):
                return False

        # boxes have digits 1--9
        for i in range(3):
            for j in range(3):
                box = set()
                i_corner, j_corner = 3 * i, 3 * j
                for ic in range(3):
                    for jc in range(3):
                        box.add(board[i_corner + ic][j_corner + jc])

                if sorted(list(set(box))) != list(range(1, len(board) + 1)):
                    return False

        return True

    def possible_nums(self, i, j, board):
        # complement of row, column, and box nums
        cant_be = set()

        # row values
        for idx, n in enumerate(board[i]):
            if n != 0 and idx != j:
                cant_be.add(n)

        # col values
        for idx, n in enumerate([board[r][j] for r in range(len(board))]):
            if n != 0 and idx != i:
                cant_be.add(n)

        # box values
        i_corner, j_corner = 3 * (i // 3), 3 * (j // 3)
        for ic in range(i_corner, i_corner + 3):
            for jc in range(j_corner, j_corner + 3):
                n = board[ic][jc]
                if n != 0 and ic != i and jc != j:
                    cant_be.add(n)

        complement = list(set(range(1, len(board) + 1)) - cant_be)
        return complement

    def first_empty_cell(self, board):
        i, j = -1, -1
        for i, board_row in enumerate(board):
            for j, board_val in enumerate(board_row):
                if board_val == 0:
                    return i, j

        return -1, -1

    def upper_left_digits(self):
        return int("".join([str(d) for d in self.solved_board[0][0:3]]))

    def show_solution(self):
        print(" " * 24 + "-" * 11)
        print(" " * 24 + "| {} |".format(self.name))
        print(" " * 24 + "-" * 11)
        print(" " * 10 + "ORIGINAL" + " " * 24 + "SOLVED")
        for i, original_row in enumerate(self.original_board):
            print(
                "{}{}{}".format(
                    original_row,
                    " --> " if i == 4 else "     ",
                    self.solved_board[i],
                )
            )
        print("\n")


def solve_boards(file_name):
    boards = {}
    with open(file_name, encoding="utf-8") as f:
        a_name, a_board = "", []
        for line in f:
            if line.find("Grid") != -1:
                if a_name:
                    boards[a_name] = a_board

                a_name = line.replace("\n", "")
                a_board = []
            else:
                row = line.replace("\n", "").split()[0]
                a_board.append([int(x) for x in row])

    # add the last game
    boards[a_name] = a_board

    res = 0
    for game_n, board in boards.items():
        s = Sudoku(game_n, board)
        s.show_solution()
        res += s.upper_left_digits()

    return res


if __name__ == "__main__":
    print(
        "Sum of upper left digits for all the solved games: {}".format(
            solve_boards("./sudoku.txt")
        )
    )
